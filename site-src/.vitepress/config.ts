import { defineConfig } from 'vitepress'

// Vite plugin: resolve broken/external imports from scraped markdown content
// as empty modules so Rollup doesn't fail.
function ignoreBrokenContentImports() {
  return {
    name: 'ignore-broken-content-imports',
    enforce: 'pre',
    resolveId(source, importer) {
      // Only intercept imports from generated entry markdown files
      if (!importer || !importer.includes('/entry/')) return null
      // Let VitePress handle its own internal modules
      if (source.startsWith('/@') || source.startsWith('virtual:') || source.startsWith('\0')) return null
      // Let normal code imports through
      if (/\.(vue|ts|js|css|scss|less|styl)$/.test(source)) return null
      // Everything else from entry pages → empty module (images, broken refs, etc.)
      if (source.startsWith('.') || source.startsWith('/')) {
        return { id: '\0ignore-broken-ref', moduleSideEffects: false, external: false }
      }
      return null
    },
    load(id) {
      if (id === '\0ignore-broken-ref') return ''
      return null
    },
  }
}

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
    plugins: [ignoreBrokenContentImports()],
  },
})
