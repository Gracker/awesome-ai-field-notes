# 文本和概念分析专家 Prompt

**来源**: GitHub Gist
**作者**: kevinz
**原文链接**: https://gist.github.com/kevinz/a191dfd758971bf31207484c34c86f30

---

## English

This is a sophisticated prompt for text analysis and interactive HTML generation. The prompt defines an AI role as a "Text Analysis Expert" with the following core capabilities:

### Core Task
When a user sends text, the AI must:
1. Deeply analyze the text content, extracting key concepts, terms, and their interrelationships.
2. Based on the analysis, generate a complete, structurally valid HTML document that helps users understand the original text through interactive and visual means.

### The HTML Gold Standard
The prompt itself is implemented as the HTML gold standard — the output must strictly follow the same structure, interaction logic, CSS style, and JavaScript libraries demonstrated in the reference page.

### Mandatory Output Format
- Every response must be a complete HTML document from `<!DOCTYPE html>` to `</html>`
- The entire HTML document must be wrapped in a Markdown code block (` ```html ... ``` `)

### HTML Generation Guidelines
1. **Responsive Design**: Layout and content must adapt to different screen sizes
2. **Mathematics**: MathJax (CHTML) must be used for rendering math formulas
3. **Code Blocks**: Must use `<pre><code class="language-LLL">` tags with syntax highlighting and horizontal scrolling
4. **Creativity and Flexibility**: Leverage HTML, CSS, and JavaScript capabilities to create informative, easy-to-understand explanatory pages

### Technical Stack
- **Viz.js**: For rendering concept relationship graphs (Graphviz-based)
- **Panzoom**: For interactive zoom/pan on the knowledge graph
- **MathJax**: For mathematical formula rendering
- **Custom CSS**: With CSS variables for theming (--rad, --text-pri, --bg-main, --brand, etc.)

### Interaction Design
- Terms in the main content area are highlighted and clickable
- Clicking a term shows detailed explanation in a side panel
- A concept relationship graph is rendered below the content
- Graph nodes are interactive — clicking shows related explanations
- Support for full-screen graph viewing with zoom/pan
- Graph layout toggle (LR/TB) and PNG download
- Google search popup for further exploration of concepts

### Concept Taxonomy
The prompt organizes concepts into types:
- **concept** (yellow): Core conceptual definitions
- **branch** (green): Task branches and sub-processes
- **tech** (blue): Technical implementation details
- **app** (red): Application-level features

## 中文

这是一个用于文本分析和交互式 HTML 生成的复杂提示词。该提示词定义了 AI 角色为"文本分析专家"，具有以下核心能力：

### 核心任务
当用户发送文本时，AI 必须：
1. 深入分析文本内容，提取关键概念、术语及其相互关系。
2. 基于分析结果，生成一个结构完整、语法有效的 HTML 文档，通过交互式和可视化的方式帮助用户理解原始文本。

### HTML 黄金标准
该提示词本身即作为 HTML 黄金标准的实现——输出必须严格遵循参考页面所展示的相同结构、交互逻辑、CSS 风格和 JavaScript 库。

### 强制输出格式
- 每个回答必须是从 `<!DOCTYPE html>` 到 `</html>` 的完整 HTML 文档
- 整个 HTML 文档必须用 Markdown 代码块包裹（` ```html ... ``` `）

### 技术栈
- **Viz.js**：渲染概念关系图（基于 Graphviz）
- **Panzoom**：知识图谱的交互式缩放/平移
- **MathJax**：数学公式渲染
- **自定义 CSS**：使用 CSS 变量实现主题化

### 交互设计
- 主内容区的术语可高亮点击
- 点击术语在侧边面板展示详细解释
- 内容下方渲染概念关系图
- 图谱节点可交互，点击展示相关解释
- 支持全屏查看图谱，可缩放和平移
- 图谱布局切换（左右/上下）和 PNG 下载
- Google 搜索弹出窗口用于进一步探索概念

### 概念分类
提示词将概念组织为以下类型：
- **concept**（黄色）：核心概念定义
- **branch**（绿色）：任务分支和子流程
- **tech**（蓝色）：技术实现细节
- **app**（红色）：应用级功能
