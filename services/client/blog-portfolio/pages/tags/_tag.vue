<template>
  <div>
    <div class="container w-full md:max-w-3xl mx-auto pt-5">
      <div
        class="w-full px-4 md:px-6 text-xl text-gray-800 leading-normal"
        style="font-family: Georgia, serif"
      >
        <h1>Showing Posts for tag: #{{ $route.params.tag }}</h1>
        <div
          v-if="posts.length === 0"
          class="flex h-96 items-center justify-center"
        >
          Sorry, no posts exists for this tag.
        </div>
      </div>
    </div>
    <ul v-if="posts.length > 0" class="divide-y divide-gray-300 -mt-10">
      <li v-for="post in posts" :key="post._id" class="py-10">
        <AppPostCard :post="post" />
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios, $recaptcha, params }) {
    if (process.client) {
      const token = await $recaptcha.execute('all')
      $axios.setHeader('X-Recaptcha-Key', token)
    }
    const posts = await $axios
      .get('/api/v1/blogs', { params: { tag: params.tag } })
      .then((response) => {
        return response.data
      })
      .catch(() => {
        return []
      })
    return { posts }
  },
  head({ params }) {
    return {
      title: `Simon's Blogs : ${this.$route.params.tag}`,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: `Various articles containing ${this.$route.params.tag}`,
        },
        {
          hid: 'keywords',
          name: 'keywords',
          content: `${this.$route.params.tag}`,
        },
        {
          hid: 'author',
          name: 'author',
          content: 'Simon Islam',
        },
      ],
    }
  },
}
</script>
