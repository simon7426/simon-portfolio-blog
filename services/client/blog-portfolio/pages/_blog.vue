<template>
  <BlogCard :post="post" />
</template>

<script>
export default {
  async asyncData({ $axios, $recaptcha, params, error }) {
    const blogId = params.blog.split('-').pop()
    if (process.client) {
      const token = await $recaptcha.execute(blogId)
      $axios.setHeader('X-Recaptcha-Key', token)
    }
    const post = await $axios
      .get(`/api/v1/blogs/${blogId}`)
      .then((response) => {
        return response.data
      })
      .catch((err) => {
        error({ statusCode: err.statusCode })
      })
    return { post }
  },
}
</script>
