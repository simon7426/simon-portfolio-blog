<template>
  <ul class="divide-y divide-gray-300 -mt-10">
    <li v-for="post in posts" :key="post._id" class="py-10">
      <AppPostCard :post="post" />
    </li>
  </ul>
</template>
<script>
export default {
  async asyncData({ $axios, $recaptcha }) {
    if (process.client) {
      const token = await $recaptcha.execute('all')
      $axios.setHeader('X-Recaptcha-Key', token)
    }
    const posts = await $axios
      .get('/api/v1/blogs')
      .then((response) => {
        return response.data
      })
      .catch(() => {
        return []
      })
    return { posts }
  },
  head() {
    return {
      title: "Simon's Blogs",
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Personal blog website. Contains blogs of various technologies and personal preferences.',
        },
        {
          hid: 'keywords',
          name: 'keywords',
          content: 'Python, Flask, FastAPI, Docker, Kubernetes',
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
