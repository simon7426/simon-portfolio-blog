import axios from 'axios/index'
import hljs from 'highlight.js'

const baseURL = process.env.BASE_URL
const browserBaseUrl = process.env.BROWSER_URL || ''

const getUrl = (post) => {
  const finalString = post.title
    .replace(/[.,/#!$%^&*;:{}=\-_'`~()]/g, '')
    .replace(/\s{2,}/g, ' ')
    .split(' ')
    .join('-')
  return '/' + finalString + '-' + post._id
}

const createSitemapRoutes = async () => {
  const routes = []
  const contents = await axios
    // .get('http://client-api:8000/api/v1/blogs')
    .get(`${baseURL}/api/v1/blogs`)
    .then((response) => {
      return response.data
    })
  const posts = contents

  for (const post of posts) {
    routes.push(getUrl(post))
  }
  return routes
}

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'blog-portfolio',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.css',
    {
      src: '~/node_modules/highlight.js/styles/night-owl.css',
      lang: 'css',
    },
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    '@nuxt/postcss8',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/moment',
    '@nuxtjs/sitemap',
    '@nuxtjs/robots',
    '@nuxtjs/markdownit',
    'nuxtjs-mdi-font',
    '@nuxtjs/axios',
    '@nuxtjs/recaptcha',
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
  sitemap: {
    hostname: browserBaseUrl,
    gzip: true,
    routes: createSitemapRoutes,
  },
  robots: [
    {
      UserAgent: '*',
      Allow: '/',
      Sitemap: `${browserBaseUrl}/sitemap.xml`,
    },
  ],
  markdownit: {
    runtime: true,
    injected: true,
    preset: 'default',
    linkify: true,
    breaks: true,
    highlight(str, lang) {
      if (lang && hljs.getLanguage(lang)) {
        try {
          return hljs.highlight(lang, str).value
        } catch (__) {}
        return ''
      }
    },
    use: [
      'markdown-it-highlightjs',
      'markdown-it-div',
      'markdown-it-attrs',
      'markdown-it-header-sections',
      'markdown-it-named-code-blocks',
      [
        'markdown-it-code-copy',
        {
          iconStyle: 'font-size: 1rem; opacity: 0.7;',
          buttonStyle:
            'position: absolute; top: 7.5px; right: 6px; cursor: pointer; outline: none; color: white;',
        },
      ],
    ],
  },
  axios: {
    baseURL: `${baseURL}`,
    browserBaseURL: `${browserBaseUrl}`,
    headers: {
      'Content-Type': 'application/json',
    },
  },
  recaptcha: {
    hideBadge: true,
    mode: 'base',
    siteKey: '6LfMGXQiAAAAAEcbzOTl9G9m21hGPUXjloZ9sUzS',
    version: 3,
  },
}
