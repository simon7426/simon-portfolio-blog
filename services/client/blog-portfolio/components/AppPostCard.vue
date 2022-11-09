<template>
  <div class="container w-full md:max-w-3xl mx-auto pt-5">
    <div
      class="w-full px-4 md:px-6 text-xl text-gray-800 leading-normal"
      style="font-family: Georgia, serif"
    >
      <div class="font-sans">
        <NuxtLink :to="getUrl(post)">
          <h1
            class="font-bold font-sans break-normal text-gray-900 pt-3 pb-2 text-3xl md:text-4xl"
          >
            {{ post.title }}
          </h1>
        </NuxtLink>
        <p class="text-sm md:text-base font-normal text-gray-600">
          Published {{ $moment(post.created_on).format('MMMM DD, YYYY') }}
        </p>
      </div>

      <p class="py-6">{{ post.summary }}...</p>

      <div class="text-base md:text-sm text-gray-500 px-4 py-6">
        Tags:
        <NuxtLink
          v-for="tag in post.tags"
          :key="tag"
          :to="'/tags/' + tag"
          class="text-base md:text-sm text-green-500 no-underline hover:underline"
          >{{ tag }}
        </NuxtLink>
      </div>
      <p class="text-base md:text-sm text-green-500 font-bold">
        <NuxtLink
          :to="getUrl(post)"
          class="text-base md:text-sm text-green-500 font-bold no-underline hover:underline"
          >Read More ></NuxtLink
        >
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
      default: () => {},
    },
  },
  methods: {
    getUrl(post) {
      const finalString = post.title
        .replace(/[.,/#!$%^&*;:{}=\-_'`~()]/g, '')
        .replace(/\s{2,}/g, ' ')
        .split(' ')
        .join('-')
      return '/' + finalString + '-' + post._id
    },
  },
}
</script>
