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
      { text: '🧠 模型 (94)', link: '/models' },
      { text: '🤖 智能体 (105)', link: '/agents' },
      { text: '💻 AI编程 (167)', link: '/coding' },
      { text: '⚡ 基础设施 (60)', link: '/infra' },
      { text: '🌍 行业观察 (54)', link: '/industry' },
      { text: '📖 学习资源 (115)', link: '/learning' },
    ],
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Gracker/awesome-ai-field-notes' },
    ],
    footer: { message: '由 OpenClaw 每日自动维护 · 16 篇有全文' },
  },
  srcDir: '.',
  outDir: '../dist',
  cleanUrls: true,
  markdown: { html: false },
  ignoreDeadLinks: true,
  vite: {
    build: {
      rollupOptions: {
        onwarn(warning, warn) {
          // Scraped content often has absolute-path refs to external CDNs
          // (/_astro/, /_next/, etc.) that Rollup can't resolve.
          // Suppress them so they don't become build errors.
          if (warning.code === 'UNRESOLVED_IMPORT' && warning.source?.startsWith('/')) {
            return
          }
          warn(warning)
        },
      },
    },
  },
})
