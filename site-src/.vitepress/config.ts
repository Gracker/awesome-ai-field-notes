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
      { text: '🧠 模型 (76)', link: '/models' },
      { text: '🤖 智能体 (140)', link: '/agents' },
      { text: '💻 AI编程 (217)', link: '/coding' },
      { text: '⚡ 基础设施 (46)', link: '/infra' },
      { text: '🌍 行业观察 (60)', link: '/industry' },
      { text: '📖 学习资源 (83)', link: '/learning' },
      { text: '🗂️ 未分类 (47)', link: '/uncategorized' },
    ],
    // Local search stays disabled: arbitrary scraped Markdown can contain empty anchors that break MiniSearch.
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Gracker/awesome-ai-field-notes' },
    ],
    footer: { message: '由 OpenClaw 每日自动维护 · 535 篇有全文' },
  },
  srcDir: '.',
  outDir: '../dist',
  cleanUrls: true,
  markdown: { html: false },
  ignoreDeadLinks: true,
})
