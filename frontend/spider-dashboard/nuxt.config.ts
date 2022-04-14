import { defineNuxtConfig } from 'nuxt3'

// https://v3.nuxtjs.org/docs/directory-structure/nuxt.config
export default defineNuxtConfig({
    head: {
        link: [
          {
            rel: 'stylesheet',
            href: "https://fonts.googleapis.com/css2?family=Roboto&display=swap"
          }
        ]
      }
})
