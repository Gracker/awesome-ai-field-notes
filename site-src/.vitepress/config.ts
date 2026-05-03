import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI Field Notes',
  description: 'AI 领域精选资源导航 — 有观点、有评分、每日自动更新',
  lang: 'zh-CN',
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
  ],
  themeConfig: {
    logo: '/favicon.svg',
    nav: [
      { text: 'GitHub', link: 'https://github.com/Gracker/awesome-ai-field-notes' },
    ],
    sidebar: [
      { text: '首页', link: '/' },
      { text: '🧠 模型 (117)', link: '/models' },
      { text: '🤖 智能体 (150)', link: '/agents' },
      { text: '💻 AI编程 (248)', link: '/coding' },
      { text: '⚡ 基础设施 (64)', link: '/infra' },
      { text: '🌍 行业观察 (66)', link: '/industry' },
      { text: '📖 学习资源 (107)', link: '/learning' },
      { text: '🗂️ 未分类 (57)', link: '/uncategorized' },
    ],
    // Local search stays disabled: arbitrary scraped Markdown can contain empty anchors that break MiniSearch.
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Gracker/awesome-ai-field-notes' },
    ],
    footer: { message: '由 OpenClaw 每日自动维护 · 605 篇有全文' },
  },
  srcDir: '.',
  outDir: '../dist',
  cleanUrls: true,
  markdown: { html: false },
  ignoreDeadLinks: true,
})
