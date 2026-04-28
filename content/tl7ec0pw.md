# OpenAI o3-mini：轻量级推理之王，STEM 领域新标杆！

> 公众号: 浮之静
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247489545&idx=1&sn=dc03ed39b015bf27e3fc75285a9e4917

---
# lencx 浅思

![Image](images/img_001.png)

从 AI 发展的现状来看，主要还是以辅助任务为主，虽说 Agent 的终极目标是自动化，但因大模型输出不可控，仍需介入人力来对其结果进行监督和修正。目前主流 AI 主要通过以下形式存在：

-   **Web 网页**：ChatGPT、Claude、Gemini、DeepSeek、豆包、千问、智谱等主流 AI 均是以在线网页为主的对话式聊天。

-   **系统应用**：一般由官方提供，相较于网页版，额外提供了一些系统访问能力，可以用来执行更复杂任务（如本地文件读写、系统通知、与第三方应用协作等）。如果按平台划分，可分为 Windows、macOS、Linux、移动端等。如果按代码实现可分为套壳或原生应用。


-   **套壳应用**：直接将网页打包成跨平台应用，不需要二次开发，也利于维护。但缺点也十分明显，不是体积过大，就是内存占用过多。常用跨平台打包框架有 Electron、Tauri 等。

-   **原生应用**：使用特定平台框架或语言进行开发（如 Swift、Kotlin 等），虽增加了维护复杂性，但往往也会提供更好的性能支持和更复杂的系统调用能力。


-   **本地应用**：为了满足特殊需求，一些用户会通过本地模型或第三方 API 来部署自己的服务。这算是比较极客的玩法了，特点是自由度更高，数据可控。至于需要交互的对话界面可通过 GitHub 找到，此领域也特卷，目前很多 AI 类开源项目都支持多模型 API 调用，以满足复杂的用户需求。

-   **AI 编程**：据我所知，AI 编程目前主要有两个方向。一种疯狂在卷本地 IDE（可以外挂 docs 等来提高编码准确性），另一种是疯狂卷在线 AI（用自然语言快速搭建网站）。


-   **本地 IDE**：GitHub Copilot\[1\]、Cursor\[2\]、Windsurf\[3\]、Trae\[4\] 等。

-   **在线 AI**：v0\[5\]、bolt.new\[6\]、Replit AI\[7\] 等。


-   ...


而 o3-mini 的强大代码能力则让我看到了新可能，它是一种介于半应用和半编程的中间态，让编程小白可以通过自然语言描述快速生成一份本地可执行的代码片段（很适合做本地化小工具或批量任务处理脚本）。这或许就是未来个人的必备技能：

-   能够将工作或生活中的部分任务抽离成需求描述给 AI，让其进行自动化处理，程序化处理似乎更准确（抽象描述需求的能力）。

-   稍微懂点编程，可以搞定本地代码运行环境，处理一些常见编程错误（知道如何将错误信息发送给 AI，让其修复）。

-   ...


这里有一个小思考：代码片段、程序运行环境、以及 AI 之间存在一些关联，似乎可以通过一个应用来进行集中化管理，这或许就是 [Noi](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIzNjE2NTI3NQ==&action=getalbum&album_id=3322583984660414465#wechat_redirect) 下一步要做的事情。

# o3-mini

OpenAI 发布了 o3-mini\[8\]，这是目前最具成本效益的推理模型（虽然价格依然高于 DeepSeek，但已远低于 o1 了。价格对比见文末附录），现已在 **ChatGPT** 和 **API** 中提供。该模型于 2024 年 12 月首次预览，专为**科学、数学和编程**任务优化，同时具备 OpenAI o1-mini 的低成本和低延迟优势（目前模型选择中已经移除了 o1-mini）。**o1 支持视觉推理但不支持联网搜索，o3-mini 支持联网搜索但不支持视觉。o1 目前仍是更广泛的常识推理模型，而 o3-mini 则为需要精度和速度的技术领域提供了专门的替代方案，大家可根据需要选择对应模型。**

![Image](images/img_002.png)

值得一提：迫于 DeepSeek 给到的压力，免费版目前可在消息输入框中选择 `推理（Reason）` 或重新生成响应来试用 OpenAI o3-mini，这是 ChatGPT 首次向免费用户提供推理模型。Plus、Team 用户使用量也从每天 50 次提升至 150 次，Pro 用户则可以无限使用 o3-mini、o3-mini-high（每月 $200 果然不是白花的），企业版将在 2 月份上线。

![Image](images/img_003.png)

刚刚 Sam 爆了一个小彩蛋（压力给到，OpenAI 也开始卖力了）：还有一个 o3-mini 的好东西即将推出——我觉得我们把最好的留到了最后！

![Image](images/img_004.png)

## 模型特性

-   **专注 STEM 领域**：数学、科学、编程能力突出，性能超越 OpenAI o1-mini，并在部分任务上匹敌 OpenAI o1。

-   **支持开发者**：支持**函数调用（Function calling\[9\]）**、**结构化输出（Structured Outputs\[10\]）**、**开发者消息（Developer Messages\[11\]）** 等，可直接用于生产环境。

-   **三种推理模式**：


-   **低推理（low）**：优先速度，适合简单任务。

-   **中等推理（medium）**：默认模型，平衡准确性和速度，等效 OpenAI o1。

-   **高推理（high）**：更强推理能力，适合复杂任务（如编程、逻辑处理等）。


-   **改进搜索**：o3-mini 可与搜索配合，查找带有相关链接的最新答案，这是 OpenAI 集成搜索功能到推理模型中的早期原型。


注：o1 模型不支持的搜索功能现已在 o3-mini 中获得支持。

![Image](images/img_005.png)

## 性能提升

-   **数学（AIME 2024）**：o3-mini（高推理）达到 87.3% 准确率，比前代模型大幅提升。低推理模式接近 o1-mini，中等推理模式接近 o1，高推理模式超越 o1。

-   **博士级科学测试（GPQA Diamond）**：o3-mini（高推理）在生物、化学、物理测试中达 79.7%，在较少的推理工作量下，性能媲美 o1（78.0%）。

-   **编程竞赛（Codeforces）**：o3-mini（高推理）在 Codeforces 竞赛编程中达 2130 Elo，比 o1-mini（1650） 高出多个级别。

-   **软件工程（SWE-bench）**：o3-mini（高推理）在 SWE-bench 任务中达到 49.3%，超过所有已发布模型。

-   **更快响应速度**：相较于 o1-mini，o3-mini（中等推理）平均快 24%，首个 token 延迟降低 2500ms，整体响应时间更短（7.7s vs 10.16s）。

-   ...


![Image](images/img_006.png)

![Image](images/img_007.png)

![Image](images/img_008.png)

![Image](images/img_009.png)

![Image](images/img_010.png)

![Image](images/img_011.png)

![Image](images/img_012.png)

![Image](images/img_013.png)

![Image](images/img_014.png)

## 安全性

采用**审议对齐**（deliberative alignment\[12\]）训练策略（即在回答用户问题前，训练模型推理人类编写的安全规范），确保更强的安全性，在越狱（Jailbreak）测试中优于 GPT-4o。

![Image](images/img_015.png)

# 案例分享

上面扯了那么多，对普通人而言并不直观。为了更好的感受 o3-mini，我测试了一些 prompt，感兴趣的朋友可以动手尝试（以下示例均为一次提问直出效果，无需多次迭代）。关于测试 prompt 的一些小技巧：

-   请在单个文件中实现代码

-   尽量不要使用依赖


## 案例

### 贪吃蛇

> 📌 Prompt
>
> V1: create a snake game, where snakes compete with each other.
>
> > 翻译：创建一个贪吃蛇游戏，让它们相互竞争。
>
> V2: add score tracking, a pause button, and a restart button.
>
> > 翻译：添加分数跟踪、暂停按钮和重启按钮。

已关注

Follow

Replay Share Like

Close

**观看更多**

更多

_退出全屏_

[](javascript:;)

_切换到竖屏全屏__退出全屏_

浮之静已关注

[](javascript:;)

Share Video

，时长01:08

0/0

00:00/01:08

切换到横屏模式

继续播放

进度条，百分之0

[Play](javascript:;)

00:00

/

01:08

01:08

[倍速](javascript:;)

_全屏_

倍速播放中

[0.5倍](javascript:;) [0.75倍](javascript:;) [1.0倍](javascript:;) [1.5倍](javascript:;) [2.0倍](javascript:;)

[超清](javascript:;) [流畅](javascript:;)

Your browser does not support video tags

继续观看

OpenAI o3-mini：轻量级推理之王，STEM 领域新标杆！

观看更多

Original

,

OpenAI o3-mini：轻量级推理之王，STEM 领域新标杆！

浮之静已关注

Share点赞Wow

Added to Top Stories[Enter comment](javascript:;)

[Video Details](javascript:;)

可将以下代码保存在本地，通过 python 命令运行。

```
import pygameimport randomimport sys# --- Game Settings ---GRID_SIZE   = 20                       # Size (in pixels) of each grid cellGRID_WIDTH  = 30                       # Number of cells horizontallyGRID_HEIGHT = 30                       # Number of cells verticallyWINDOW_WIDTH  = GRID_WIDTH * GRID_SIZEWINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZEFPS = 10                               # Game speed (frames per second)# --- Colors ---BLACK   = (0, 0, 0)WHITE   = (255, 255, 255)RED     = (255, 0, 0)GREEN   = (0, 255, 0)BLUE    = (0, 0, 255)YELLOW  = (255, 255, 0)GRAY    = (100, 100, 100)# --- Directions ---UP    = (0, -1)DOWN  = (0, 1)LEFT  = (-1, 0)RIGHT = (1, 0)# --- Snake Class ---class Snake:    def __init__(self, start_pos, color):        self.body = [start_pos]      # The snake is a list of (x,y) positions        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])        self.color = color        self.alive = True        self.score = 0    def get_head(self):        return self.body[0]    def move(self, grow=False):        """Advance the snake one step in its current direction.           If grow is True, the snake’s tail is not removed."""        if not self.alive:            return        head_x, head_y = self.get_head()        dx, dy = self.direction        new_head = (head_x + dx, head_y + dy)        self.body.insert(0, new_head)        if not grow:            self.body.pop()    def set_direction(self, new_direction):        """Set a new direction for the snake. Prevent reversing if length > 1."""        if len(self.body) > 1:            cur_dx, cur_dy = self.direction            # Prevent 180° turn:            if (cur_dx * -1, cur_dy * -1) == new_direction:                return        self.direction = new_direction    def is_direction_safe(self, direction, snakes):        """Check if moving in the given direction would cause an immediate collision."""        head_x, head_y = self.get_head()        dx, dy = direction        new_head = (head_x + dx, head_y + dy)        # Check board boundaries        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):            return False        # Check collision with any snake’s body (including self)        for snake in snakes:            if new_head in snake.body:                return False        return True    def update_ai(self, food_list, snakes):        """Simple AI: choose a direction that moves toward the closest food.           If that direction isn’t safe, try the other options."""        if not food_list:            return        head = self.get_head()        # Find the food item with the smallest Manhattan distance:        closest_food = min(food_list, key=lambda f: abs(f[0]-head[0]) + abs(f[1]-head[1]))        dx = closest_food[0] - head[0]        dy = closest_food[1] - head[1]        # Build a prioritized list of directions toward the food:        possible_directions = []        if dx > 0:            possible_directions.append(RIGHT)        elif dx < 0:            possible_directions.append(LEFT)        if dy > 0:            possible_directions.append(DOWN)        elif dy < 0:            possible_directions.append(UP)        # Append the remaining directions:        for d in [UP, DOWN, LEFT, RIGHT]:            if d not in possible_directions:                possible_directions.append(d)        # Choose the first safe direction:        for d in possible_directions:            if self.is_direction_safe(d, snakes):                self.set_direction(d)                return        # If no “preferred” direction is safe, pick any safe direction:        safe_dirs = [d for d in [UP, DOWN, LEFT, RIGHT] if self.is_direction_safe(d, snakes)]        if safe_dirs:            self.set_direction(random.choice(safe_dirs))        # Otherwise, no safe move is available; the snake will collide soon.# --- Game Class ---class Game:    def __init__(self):        pygame.init()        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))        pygame.display.set_caption("Autonomous Snake Competition")        self.clock = pygame.time.Clock()        self.font = pygame.font.SysFont(None, 24)        self.init_game_state()    def init_game_state(self):        """Initialize or reset the game state (snakes, food, pause flag)."""        # Create several snakes with different starting positions and colors:        self.snakes = []        colors = [GREEN, BLUE, YELLOW, RED]        starting_positions = [            (5, 5),            (GRID_WIDTH - 6, GRID_HEIGHT - 6),            (5, GRID_HEIGHT - 6),            (GRID_WIDTH - 6, 5)        ]        for i in range(len(colors)):            self.snakes.append(Snake(starting_positions[i], colors[i]))        self.food_list = []        self.spawn_food(count=5)  # Start with 5 food items        # Game control flags        self.paused = False    def reset(self):        """Restart the game by reinitializing the game state."""        self.init_game_state()    def spawn_food(self, count=1):        """Spawn the given number of food items."""        for _ in range(count):            self.add_food()    def add_food(self):        """Place a food item at a random empty cell."""        while True:            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))            # Ensure no snake occupies this cell and it isn’t already food            collision = any(pos in snake.body for snake in self.snakes) or pos in self.food_list            if not collision:                self.food_list.append(pos)                break    def draw_scores(self):        """Render the score for each snake on the screen."""        y_offset = 5        for i, snake in enumerate(self.snakes):            status = "Alive" if snake.alive else "Dead"            text_str = f"Snake {i+1} Score: {snake.score} ({status})"            text = self.font.render(text_str, True, WHITE)            self.screen.blit(text, (5, y_offset))            y_offset += 20    def draw_instructions(self):        """Display instructions for pausing and restarting."""        instructions = "Press 'P' to pause/resume, 'R' to restart"        text = self.font.render(instructions, True, WHITE)        self.screen.blit(text, (5, WINDOW_HEIGHT - 25))    def run(self):        running = True        while running:            self.clock.tick(FPS)            # --- Event Handling ---            for event in pygame.event.get():                if event.type == pygame.QUIT:                    running = False                elif event.type == pygame.KEYDOWN:                    if event.key == pygame.K_p:                        self.paused = not self.paused                    elif event.key == pygame.K_r:                        self.reset()            if not self.paused:                # Update AI for each alive snake                alive_snakes = [snake for snake in self.snakes if snake.alive]                random.shuffle(alive_snakes)                for snake in alive_snakes:                    snake.update_ai(self.food_list, self.snakes)                # Move each snake and check for collisions                for snake in alive_snakes:                    if not snake.alive:                        continue                    head_before = snake.get_head()                    new_head = (head_before[0] + snake.direction[0], head_before[1] + snake.direction[1])                    # Check wall collisions                    if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):                        snake.alive = False                        continue                    # Check collisions with any snake’s body (using the current board state)                    collision = False                    for other in self.snakes:                        if new_head in other.body:                            collision = True                            break                    if collision:                        snake.alive = False                        continue                    # Check if food is at the new head position:                    if new_head in self.food_list:                        snake.move(grow=True)                        snake.score += 1                        self.food_list.remove(new_head)                        self.add_food()  # Replace the eaten food                    else:                        snake.move(grow=False)            # --- Rendering ---            self.screen.fill(BLACK)            # Draw food items            for food in self.food_list:                rect = pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)                pygame.draw.rect(self.screen, RED, rect)            # Draw each snake            for snake in self.snakes:                color = snake.color if snake.alive else GRAY                for segment in snake.body:                    rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)                    pygame.draw.rect(self.screen, color, rect)            # Draw the scoreboard and instructions            self.draw_scores()            self.draw_instructions()            # If paused, overlay a pause message            if self.paused:                pause_text = self.font.render("Paused", True, WHITE)                text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))                self.screen.blit(pause_text, text_rect)            pygame.display.flip()        pygame.quit()        # --- Final Score Display ---        print("\n--- Final Scores ---")        for i, snake in enumerate(self.snakes):            status = "Alive" if snake.alive else "Dead"            print(f"Snake {i + 1} ({snake.color}): Score = {snake.score} ({status})")# --- Run the Game ---if __name__ == "__main__":    game = Game()    game.run()
```

### 彩球碰撞

> 📌 Prompt
>
> Create a p5.js script that generates 100 colorful balls bouncing inside a slowly rotating sphere. Each ball should leave a fading trail, and collisions with the sphere boundary should trigger a particle effect scaled by collision strength. Ensure accurate collision detection so the balls remain within the sphere.
>
> > 翻译：创建一个 p5.js 脚本，生成 100 个彩色球，它们在缓慢旋转的球体内弹跳。每个球都应留下一条逐渐消失的轨迹，与球体边界的碰撞应触发按碰撞强度缩放的粒子效果。确保准确的碰撞检测，使球保持在球体内。

已关注

Follow

Replay Share Like

Close

**观看更多**

更多

_退出全屏_

