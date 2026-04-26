# 理解llama.cpp怎么完成大模型推理的
> 原文链接: https://zhuanlan.zhihu.com/p/996110863?utm_medium=social&utm_psn=1849039234352156672&utm_source=wechat_session

---

> 原文链接: https://zhuanlan.zhihu.com/p/996110863

---
原文： （已经获得原作者的翻译授权）

[Understanding how LLM inference works with llama.cpp](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/)

_译者的话: llama.cpp出道以来，很少有官方文档，但是本文通过代码驱动的讲解， 讲清楚了llama.cpp的原理，个人推荐一读。_

在这篇文章中，我们将深入探讨大型语言模型（LLMs）的内部结构，以便更好地理解它们是如何工作的。为帮助我们进行这次探索，我们将使用 llama.cpp 的源码，它是 Meta 的 LLaMA 模型的纯 C++ 实现。作者个人认为，llama.cpp 是理解 LLM 深层原理的一个优秀学习工具，它的代码简洁明了，不涉及过多的抽象。我们将使用特定的提交版本。

本文的重点是 LLM 的推理部分，即：已训练好的模型如何基于用户输入的提示生成响应。这篇文章主要写给那些非机器学习和人工智能领域的工程师，旨在帮助他们更好地理解 LLM，**本文从工程角度而非 AI 角度探讨 LLM 的内部工作原理，因此不要求读者具备深厚的数学或深度学习知识**。（_译者：这正是本文最妙的地方_）在文章中，我们将从头到尾介绍 LLM 的推理过程，涵盖以下主题：

1.  [张量](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/%23understanding-tensors-with-ggml)：概述数学运算如何以张量的形式实现， 并可能潜在转移到 GPU 上处理。
2.  [分词](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/%23tokenization)：将用户输入的提示分解为令牌列表，LLM 使用这些令牌作为输入。
3.  **嵌入Embedding：将令牌转换为高维向量的过程。**
4.  [Transformer](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/%23the-transformer)：大语言模型架构的核心部分，负责实际的推理过程，我们将重点介绍自注意力机制。
5.  [采样](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/%23sampling)：选择下一个预测令牌的过程，我们将探讨两种采样技术。
6.  [KV 缓存](https://link.zhihu.com/?target=https%3A//www.omrimallis.com/posts/understanding-how-llm-inference-works-with-llama-cpp/%23optimizing-inference)：一种常见的优化技术，用于加快长提示的推理速度，我们将介绍一个基本的 kv 缓存实现。

通过阅读本文，你将有望对 LLM 的工作过程有一个端到端的理解，并且能够探索更高级的主题，这些主题将在最后一节中详细说明。

## 从提示到输出的高级流程

作为一个大型语言模型（LLM），LLaMA 的工作原理是接收一个输入文本（即“提示”），并预测下一个应该生成的标记（token）或词汇。

为了说明这个过程，我们以维基百科量子力学条目中的第一句话为例。我们的提示是：

> **Quantum mechanics is a fundamental theory in physics that**

LLM 会尝试根据训练时学到的知识继续这句话。使用 llama.cpp，我们得到如下的续写：

> **provides insights into how matter and energy behave at the atomic scale.**

让我们先来看一下这个过程的高级流程。LLM 的核心功能是每次只预测一个标记。生成完整的句子（或更多内容）是通过反复应用 LLM 模型到相同的提示上，并将之前的输出标记附加到提示后形成的。这种模型被称为自回归模型。因此，我们主要关注单个标记的生成，流程可以简化为以下高级图所示：
_LLM 通过每次迭代生成一个标记，然后将其添加到输入提示中，不断重复该过程，直到生成完整的输出。这就是 LLM 如何从输入提示生成文本的基础。_

![](https://pic3.zhimg.com/v2-882ac5a7962433e1293ea4eb419b0ba6_1440w.jpg)

从用户提示生成单个标记的完整流程包括多个阶段，如分词、嵌入、Transformer 神经网络和采样。本文将介绍这些阶段。

根据图示，整个流程如下：

1.  **分词**：分词器将提示分解为一个标记列表。根据模型的词汇表，某些单词可能会被分解成多个标记。每个标记由一个唯一的数字表示。
2.  **嵌入embedding转换**：每个数字标记被转换为一个嵌入向量。嵌入是一个固定大小的向量，以一种更适合 LLM 处理的方式表示标记。所有嵌入向量组合在一起形成嵌入矩阵。
3.  **输入 Transformer**：嵌入矩阵作为 Transformer 的输入。Transformer 是 LLM 的核心神经网络，由多层链组成。每一层接收输入矩阵，并利用模型参数执行各种数学运算，最主要的是自注意力机制。该层的输出作为下一层的输入。
4.  **logits 生成**：最后的神经网络将 Transformer 的输出转换为 logits。每个可能的下一个标记都有一个相应的 logits，表示该标记作为句子“正确”延续的概率。
5.  **采样**：使用多种采样技术之一，从 logits 列表中选择下一个标记。
6.  **生成输出**：所选标记作为输出返回。要继续生成更多的标记，所选标记会被附加到第 1 步的标记列表中，然后重复该过程。这可以一直进行，直到生成所需数量的标记，或者 LLM 发出特殊的结束流（EOS）标记。

接下来的部分将详细探讨这些步骤。但在此之前，我们需要熟悉张量的概念。

## 理解张量及其在 ggml 中的应用

张量是神经网络中执行数学运算的主要数据结构。**llama.cpp** 使用的是 **ggml**，这是一种纯 C++ 实现的张量库，相当于 Python 生态系统中的 **PyTorch** 或 **TensorFlow**。我们将通过 ggml 来理解张量是如何操作的。

张量可以表示一个多维数组的数值。它可能包含一个单一的数值（标量）、一个向量（一维数组）、一个矩阵（二维数组）甚至是三维或四维数组。通常，实际应用中不需要使用更多维度。

理解两种类型的张量是非常重要的：

1.  **数据张量**：这些张量持有实际数据，包含一个多维数组的数值。
2.  **运算张量**：这些张量仅表示一个或多个其他张量之间运算的结果，只有在实际计算时才会包含数据。

我们接下来将详细探讨这两类张量之间的区别。

### 张量的基本结构

在 **ggml** 中，张量由 `ggml_tensor` 结构体表示。为便于理解，我们稍微简化了一下它的结构，简化后的样子如下：

```c
// ggml.h
struct ggml_tensor {
    enum ggml_type    type;
    enum ggml_backend backend;

    int     n_dims; //张量的维度数量，例如一维向量、二维矩阵等
    // number of elements
    int64_t ne[GGML_MAX_DIMS];
    // stride in bytes
    size_t  nb[GGML_MAX_DIMS];

    enum ggml_op op; // 表示张量是哪个操作的结果（例如加法、乘法等）

    struct ggml_tensor * src[GGML_MAX_SRC];// 张量的输入源（如果它是计算结果）

    void * data; //指向实际数据的指针，可能是 NULL，如果该张量仅代表一个操作的结果

    char name[GGML_MAX_NAME];
};
```

前几个字段比较容易理解：

-   **type**：包含张量元素的基本类型。例如，`GGML_TYPE_F32` 表示每个元素是一个 32 位浮点数， 也可以是F16或者其他整形量化。
-   **ggml\_backend**：指示张量是基于 CPU 还是基于 GPU 存储的。我们稍后会讨论这一点。
-   **n\_dims**：张量的维度数量，可以是 1 到 4 维。
-   **ne**：表示每个维度中的元素数量。ggml 采用行优先顺序，意味着 `ne[0]` 表示每行的大小，`ne[1]` 表示每列的大小，依此类推。
-   **nb**：这个字段稍微复杂一些，它包含步长信息，即每个维度中连续元素之间的字节数。在第一个维度中，步长等于元素的大小；在第二个维度中，它等于每行的大小乘以元素的大小，以此类推。

-   例如，对于一个 4x3x2 的张量：

![](https://picx.zhimg.com/v2-f59f10c3215d5dae2b0087eccb132e1f_1440w.jpg)

一个 32 位浮点数张量的例子，维度为 {4, 3, 2}，步长为 {4, 16, 48}。

使用步长的目的是为了在进行某些张量操作时无需复制任何数据。例如，在二维张量上执行转置操作，将行转换为列时，只需要交换 `ne`（维度大小）和 `nb`（步长），而指向相同的底层数据即可实现这个操作，无需对数据本身进行复制。

```c
// ggml.c (the function was slightly simplified).
struct ggml_tensor * ggml_transpose(
        struct ggml_context * ctx,
        struct ggml_tensor  * a) {
    // Initialize `result` to point to the same data as `a`
    struct ggml_tensor * result = ggml_view_tensor(ctx, a);

    result->ne[0] = a->ne[1];
    result->ne[1] = a->ne[0];

    result->nb[0] = a->nb[1];
    result->nb[1] = a->nb[0];

    result->op   = GGML_OP_TRANSPOSE;
    result->src[0] = a;

    return result;
}
```

在上述函数中，`result` 是一个新张量，它被初始化为指向与源张量 `a` 相同的多维数值数组。通过交换 `ne`（维度大小）和 `nb`（步长），可以执行转置操作，而无需复制任何数据。

_译者注：这里ggml\_view\_tensor和GGML\_OP\_TRANSPOSE发挥了重要作用， **ggml\_view\_tensor**： `ggml_view_tensor`函数创建了一个新的张量`result`，这个张量指向原始张量`a`的相同数据。这意味着`result`和`a`共享相同的内存空间，但它们的维度和步长可以不同。将 `result->op` 设置为 `GGML_OP_TRANSPOSE` 之后，`ggml` 系统知道这个张量是通过转置另一个张量得到的，而不是一个直接包含数据的张量。这个标记在后续的计算中很重要，因为 `ggml` 在需要计算时会按照这个操作类型来执行相应的计算逻辑。这在后面会马上讲到。_

### 张量操作与视图

正如之前提到的，有些张量包含实际数据，而另一些张量则表示其他张量之间运算的理论结果。回到 `ggml_tensor` 结构体：

-   **`op`**：可以是张量之间支持的任何操作。如果设置为 `GGML_OP_NONE`，则表示张量包含数据。其他值表示不同的操作。例如，`GGML_OP_MUL_MAT` 表示该张量不包含数据，而是表示两个其他张量之间矩阵乘法的结果。
-   **`src`**：这是一个指向要进行运算的张量的指针数组。例如，如果 `op == GGML_OP_MUL_MAT`，那么 `src` 将包含指向两个要相乘的张量的指针。如果 `op == GGML_OP_NONE`，则 `src` 为空。
-   **`data`**：指向实际张量数据的指针，如果该张量表示一个操作，则为 `NULL`。它也可能指向另一个张量的数据，在这种情况下，它被称为视图。例如，在上面的 `ggml_transpose()` 函数中，结果张量就是原始张量的视图，只是维度和步长被交换了。`data` 指向相同的内存位置。

矩阵乘法函数很好地展示了这些概念：通过指向相同的数据并修改维度和步长，张量可以通过视图避免数据复制。

```c
// ggml.c (simplified and commented)
struct ggml_tensor * ggml_mul_mat(
        struct ggml_context * ctx,
        struct ggml_tensor  * a,
        struct ggml_tensor  * b) {
    // Check that the tensors' dimensions permit matrix multiplication.
    GGML_ASSERT(ggml_can_mul_mat(a, b));

    // Set the new tensor's dimensions
    // according to matrix multiplication rules.
    const int64_t ne[4] = { a->ne[1], b->ne[1], b->ne[2], b->ne[3] };
    // Allocate a new ggml_tensor.
    // No data is actually allocated except the wrapper struct.
    struct ggml_tensor * result = ggml_new_tensor(ctx, GGML_TYPE_F32, MAX(a->n_dims, b->n_dims), ne);

    // Set the operation and sources.
    result->op   = GGML_OP_MUL_MAT;
    result->src[0] = a;
    result->src[1] = b;

    return result;
}
```

在上述函数中，`result` 不包含任何数据。它只是表示矩阵 `a` 和 `b` 相乘后的理论结果。

### 计算张量

上面的 `ggml_mul_mat()` 函数或其他任何张量操作，都不会立即进行计算，它只是为操作准备好张量。换一种方式理解，它是在构建一个计算图，其中每个张量操作都是一个节点，操作的来源是该节点的子节点。在矩阵乘法的情况下，计算图会有一个父节点，其操作为 `GGML_OP_MUL_MAT`，同时有两个子节点。

在 `llama.cpp` 中的一个实际例子中，下面的代码实现了自注意力机制，这是每个 Transformer 层的一部分，后续会对此进行更深入的探讨：

```c
// llama.cpp
static struct ggml_cgraph * llm_build_llama(/* ... */) {
    // ...

    // K,Q,V are tensors initialized earlier
    struct ggml_tensor * KQ = ggml_mul_mat(ctx0, K, Q);
    // KQ_scale is a single-number tensor initialized earlier.
    struct ggml_tensor * KQ_scaled = ggml_scale_inplace(ctx0, KQ, KQ_scale);
    struct ggml_tensor * KQ_masked = ggml_diag_mask_inf_inplace(ctx0, KQ_scaled, n_past);
    struct ggml_tensor * KQ_soft_max = ggml_soft_max_inplace(ctx0, KQ_masked);
    struct ggml_tensor * KQV = ggml_mul_mat(ctx0, V, KQ_soft_max);

    // ...
}
```

这段代码是一系列张量操作，并构建了一个计算图，与原始 Transformer 论文中描述的计算图完全一致。

![](images/img_003.jpg)

要实际计算结果张量（这里是 KQV），需要执行以下步骤：

1.  **加载数据**：数据被加载到每个叶子张量的 `data` 指针中。在这个例子中，叶子张量是 K、Q 和 V。
2.  **构建计算图**：使用 `ggml_build_forward()` 函数将输出张量（KQV）转换为计算图。这个函数比较简单，以深度优先顺序排列节点。
3.  **运行计算图**：通过 `ggml_graph_compute()` 运行计算图，该函数对每个节点执行 `ggml_compute_forward()` 操作，按深度优先顺序计算。`ggml_compute_forward()` 负责主要的数学计算，完成数学运算并将结果填充到张量的 `data` 指针中。
4.  **结果输出**：在这个过程结束时，输出张量的 `data` 指针指向最终计算结果。

### 将计算任务转移到 GPU

由于 GPU 的高度并行性，许多张量操作（如矩阵加法和乘法）可以在 GPU 上更高效地完成。当 GPU 可用时，可以将张量标记为 `tensor->backend = GGML_BACKEND_GPU`。在这种情况下`ggml_compute_forward()` 会尝试将计算任务转移到 GPU 进行。GPU 会执行张量操作，并将结果存储在 GPU 的内存中（而不是张量的 `data` 指针中）。

例如，在之前的自注意力计算图中，假设 K、Q、V 是固定的张量，计算可以转移到 GPU 上完成。

![](https://pic2.zhimg.com/v2-ba3f18d641eaea05f86adce77e1ab6a3_1440w.jpg)

这个过程首先将 K、Q、V 复制到 GPU 内存中。然后由 CPU 按照张量逐个驱动计算，但实际的数学运算会被转移到 GPU 进行。当计算图中的最后一个操作完成时，结果张量的数据会从 GPU 内存复制回 CPU 内存。

**注意**：在实际的 Transformer 中，K、Q、V 并不是固定的，KQV 也不是最终的输出。后面我们将对此进行详细说明。

在理解了张量的工作机制之后，我们可以回到 LLaMA 的流程。

## 分词Tokenization

推理的第一步是分词。分词是将提示（prompt）拆分为称为“词元”的较短字符串列表的过程。词元必须是模型词汇表的一部分，词汇表是LLM（大型语言模型）在训练时使用的词元列表。例如，LLaMA的词汇表由32,000个词元组成，随模型一同分发。

对于我们的示例提示，分词将提示拆分为11个词元（空格被替换为特殊的元符号‘▁’ (U+2581)）：

> |Quant|um|▁mechan|ics|▁is|▁a|▁fundamental|▁theory|▁in|▁physics|▁that|

在分词过程中，LLaMA使用了基于字节对编码（[BPE](https://zhida.zhihu.com/search?content_id=249181997&content_type=Article&match_order=1&q=BPE&zhida_source=entity)）算法的SentencePiece分词器。这种分词器非常有趣，因为它是基于子词的，这意味着一个词可能由多个词元表示。例如，在我们的提示中，‘Quantum’被拆分为‘Quant’和‘um’。在训练过程中，词汇表的生成通过BPE算法保证常用词作为单个词元包含在词汇表中，而罕见词则被分解为子词。在上面的示例中，单词‘Quantum’不在词汇表中，但‘Quant’和‘um’作为两个独立的词元存在。空格不会被特殊处理，它们如果足够常见，也会作为元字符包含在词元中。

基于子词的分词具有多种优势：

它允许LLM学习像‘Quantum’这样的罕见词的含义，同时通过将常见的后缀和前缀表示为独立词元，保持词汇表的相对小型化。 它无需使用语言特定的分词方案即可学习语言特定的特性。引用BPE编码论文中的例子： 考虑德语的复合词如Abwasser|behandlungs|anlange（污水处理厂），分段的、可变长度的表示形式比将该词编码为固定长度的向量更加直观。

同样，这种分词方式在解析代码时也非常有用。例如，一个名为model\_size的变量将被分词为model|\_|size，这使得LLM能够“理解”该变量的用途（这也是为变量赋予有意义名称的另一个原因！）。 在llama.cpp中，分词是通过llama\_tokenize()函数完成的。该函数接受提示字符串作为输入，并返回词元列表，其中每个词元由一个整数表示。

```c
// llama.h
typedef int llama_token;

// common.h
std::vector<llama_token> llama_tokenize(
        struct llama_context * ctx,
        // the prompt
        const std::string & text,
        bool   add_bos);
```

分词过程首先将提示拆分为单个字符的词元。接着，它会迭代地尝试将每两个连续的词元合并为一个更大的词元，只要合并后的词元是词汇表的一部分。这样可以确保生成的词元尽可能大。对于我们的示例提示，分词步骤如下：

```text
Q|u|a|n|t|u|m|▁|m|e|c|h|a|n|i|c|s|▁|i|s|▁a|▁|f|u|n|d|a|m|e|n|t|a|l|

Qu|an|t|um|▁m|e|ch|an|ic|s|▁|is|▁a|▁f|u|nd|am|en|t|al|

Qu|ant|um|▁me|chan|ics|▁is|▁a|▁f|und|am|ent|al|

Quant|um|▁mechan|ics|▁is|▁a|▁fund|ament|al|

Quant|um|▁mechan|ics|▁is|▁a|▁fund|amental|

Quant|um|▁mechan|ics|▁is|▁a|▁fundamental|
```

请注意，每个中间步骤都符合模型词汇表的有效分词规则。然而，只有最后一步会被用作LLM（大型语言模型）的输入。

## 嵌入embedding

这些词元将作为LLaMA的输入，用于预测下一个词元。此处的关键函数是llm\_build\_llama()函数：

```c
// llama.cpp (simplified)
static struct ggml_cgraph * llm_build_llama(
         llama_context & lctx,
     const llama_token * tokens,
                   int   n_tokens,
                   int   n_past);
```

该函数接受由`tokens`和`n_tokens`参数表示的词元列表作为输入。然后，它构建LLaMA的完整张量计算图，并将其作为`ggml_cgraph`结构返回。在此阶段实际上并不会进行任何计算。目前可以忽略`n_past`参数，它目前设置为零。稍后我们在讨论`kv cache`时将再次提到它。

除了词元，该函数还使用模型权重或模型参数。这些是LLM（大型语言模型）在训练过程中学习的固定张量，作为模型的一部分包含在内。这些模型参数在推理开始前预先加载到`lctx`中。

现在我们将开始探索计算图结构。该计算图的第一部分涉及将词元转换为嵌入。嵌入是每个词元的固定向量表示，它比纯整数更适合深度学习，因为它捕捉到了单词的语义意义。该向量的大小是模型维度，不同模型之间有所不同。例如，在LLaMA-7B中，模型维度为`n_embd=4096`。模型参数包括一个将词元转换为嵌入的词元嵌入矩阵。由于我们的词汇大小为`n_vocab=32000`，因此这是一个32000 x 4096的矩阵，每一行都包含一个词元的嵌入向量：

![](https://picx.zhimg.com/v2-90e4f2bca86c84958cc6ff32e8f2ca2f_1440w.jpg)

每个词元都有一个在训练过程中学习到的关联嵌入，可以通过词元嵌入矩阵进行访问。

计算图的第一部分从词元嵌入矩阵中提取每个词元的相关行：

```c
// llama.cpp (simplified)
static struct ggml_cgraph * llm_build_llama(/* ... */) {
    // ...

    struct ggml_tensor * inp_tokens = ggml_new_tensor_1d(ctx0, GGML_TYPE_I32, n_tokens);
    memcpy(
        inp_tokens->data,
        tokens,
        n_tokens * ggml_element_size(inp_tokens));

    inpL = ggml_get_rows(ctx0, model.tok_embeddings, inp_tokens);
}
//
```

代码首先创建一个名为`inp_tokens`的新的一维整数张量，用于存储数值化的词元。接着，它将词元值复制到该张量的数据指针中。最后，它创建了一个新的`GGML_OP_GET_ROWS`张量操作，将词元嵌入矩阵`model.tok_embeddings`与我们的词元组合起来。

当稍后计算该操作时，它将从嵌入矩阵中提取相应的行，如上图所示，创建一个新的`n_tokens x n_embd`矩阵，仅包含按原始顺序排列的词元嵌入：

![](images/img_006.jpg)

嵌入过程为每个原始词元创建一个固定大小的嵌入向量。当这些向量堆叠在一起时，它们构成了提示（prompt）的嵌入矩阵。

## Transformer

计算图的主要部分被称为Transformer。Transformer是一种神经网络架构，是大型语言模型（LLM）的核心，负责执行主要的推理逻辑。在接下来的部分中，我们将从工程角度探讨Transformer的一些关键方面，重点关注自注意力机制。如果你想对Transformer架构有直观的了解，我建议阅读《[The Illustrated Transformer](https://link.zhihu.com/?target=https%3A//jalammar.github.io/illustrated-transformer/)》。

### 自注意力机制

我们首先深入了解下什么是自注意力机制，然后再回顾它在整体Transformer架构中的作用。

自注意力机制是一种机制，它接收一系列词元，并生成该序列的紧凑向量表示，考虑到词元之间的关系。这是LLM架构中唯一计算词元间关系的地方，因此它构成了语言理解的核心，涵盖了对词汇关系的理解。由于涉及跨词元的计算，从工程角度来看，它也是最有趣的部分，尤其是对于较长序列来说，计算量可能会非常大。

自注意力机制的输入是`n_tokens x n_embd`的嵌入矩阵，其中每一行或向量表示一个独立的词元。这些向量中的每一个都将被转换为三个不同的向量，分别称为“键”（key）、“查询”（query）和“值”（value）向量。这种转换通过将每个词元的嵌入向量与固定的`wk`、`wq`和`wv`矩阵（这些矩阵是模型参数的一部分）相乘来实现：

![](https://pica.zhimg.com/v2-1725dd15396d0e243d88240c0b38c42e_1440w.jpg)

将词元的嵌入向量与wk、wq和wv参数矩阵相乘，会为该词元生成“键”（key）、“查询”（query）和“值”（value）向量。

这个过程会对每个词元重复进行，也就是执行n\_tokens次。理论上可以通过循环来完成，但为了提高效率，所有行会通过矩阵乘法在一次操作中进行转换，矩阵乘法正是实现这一点的。相关代码如下所示：

```c
// llama.cpp (simplified to remove use of cache)

// `cur` contains the input to the self-attention mechanism
struct ggml_tensor * K = ggml_mul_mat(ctx0,
    model.layers[il].wk, cur);
struct ggml_tensor * Q = ggml_mul_mat(ctx0,
    model.layers[il].wq, cur);
struct ggml_tensor * V = ggml_mul_mat(ctx0,
    model.layers[il].wv, cur);
```

最终，我们得到三个矩阵 K、Q 和 V，它们的大小均为 `n_tokens x n_embd`，分别包含每个词元的键（key）、查询（query）和值（value）向量堆叠在一起。

自注意力机制的下一步是将包含查询向量的矩阵 Q 与包含键向量的矩阵 K 的转置相乘。对于不太熟悉矩阵操作的人来说，此操作实际上是为每对查询和键向量计算一个联合得分。我们使用符号 S(i,j) 来表示查询 i 与键 j 的得分。

这个过程生成了 `n_tokens^2` 个得分，每个查询-键对都有一个得分，并将其打包在一个称为 KQ 的矩阵中。随后，该矩阵会进行掩码操作，以移除对角线以上的元素：

![](https://picx.zhimg.com/v2-dc0eb1ea398f43f0cefcbef68736078b_1440w.jpg)

通过将矩阵 Q 与 K 的转置相乘，计算每个查询-键对的联合得分 S(i,j)。此处显示的是前四个词元的结果，以及每个得分所对应的词元。掩码步骤确保仅保留每个词元与其前面词元之间的得分。为了简化说明，省略了中间的缩放操作。

掩码操作是一个关键步骤。对于每个词元，它只保留与其前面词元之间的得分。在训练阶段，这一约束确保LLM仅根据之前的词元预测当前词元，而不是未来的词元。此外，正如我们稍后将更详细探讨的，它还允许在预测未来词元时进行显著优化。

自注意力机制的最后一步是将掩码后的得分矩阵`KQ_masked`与之前的值向量相乘。这样的矩阵乘法操作会生成所有前面词元值向量的加权和，其中权重是得分`S(i,j)`。例如，对于第四个词元“ics”，它会生成“Quant”、“um”、“▁mechan”和“ics”这几个词元的值向量的加权和，权重为`S(3,0)`到`S(3,3)`，这些得分是由“ics”的查询向量与之前所有词元的键向量计算出来的。

![](https://pic2.zhimg.com/v2-c14f4b494e34b92eb144de6c2a09b9d7_1440w.jpg)

KQV矩阵包含了值向量的加权和。例如，突出显示的最后一行是前四个值向量的加权和，权重为对应的突出显示的得分。

KQV矩阵标志着自注意力机制的结束。之前我们已经在一般张量计算的上下文中介绍了实现自注意力机制的相关代码，但现在你能够更好地理解它。

### Transformer的层

自注意力机制是Transformer层的一个组成部分。每一层除了自注意力机制外，还包含多个其他的张量操作，主要是矩阵加法、乘法和激活函数操作，这些都是前馈神经网络的一部分。我们不会详细探讨这些操作，只需要注意以下几点：

-   前馈网络中使用了大型、固定的参数矩阵。在LLaMA-7B中，这些矩阵的大小为`n_embd x n_ff = 4096 x 11008`。
-   除了自注意力机制之外，其他所有操作都可以看作是逐行或逐词元进行的。正如之前提到的，只有自注意力机制包含跨词元的计算。这一点在后面讨论kv缓存时会非常重要。
-   输入和输出的大小始终为`n_tokens x n_embd`：每个词元对应一行，每行的大小等于模型的维度。

为完整起见，我还包含了LLaMA-7B中单个Transformer层的图示。请注意，未来的模型架构可能会稍有不同。

![](https://pic1.zhimg.com/v2-be9adf7ce707de52b0675e3edf9b9394_1440w.jpg)

LLaMA-7B中一个Transformer层的完整计算图，包含自注意力机制和前馈机制。每一层的输出作为下一层的输入。在自注意力阶段和前馈阶段都使用了大型参数矩阵，这些矩阵构成了该模型的大部分70亿个参数。

在Transformer架构中有多个层。例如，在LLaMA-7B中有32个层（n\_layers=32）。这些层是相同的，除了每层都有自己的一组参数矩阵（例如用于自注意力机制的各自的`wk`、`wq`和`wv`矩阵）。第一层的输入是上文描述的嵌入矩阵。第一层的输出随后被用作第二层的输入，依此类推。我们可以将其看作每一层都生成了一组嵌入，但这些嵌入不再直接与单个词元相关，而是与词元关系的某种更复杂的理解相关联。