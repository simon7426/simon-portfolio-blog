<template>
  <div class="space-y-4 pb-2">
    <div class="flex">
      <div class="flex-shrink-0 mr-3">
        <img
          class="mt-2 rounded-full w-8 h-8 sm:w-10 sm:h-10"
          :src="`https://www.gravatar.com/avatar/${getMailHash}`"
          alt=""
        />
      </div>
      <div
        class="flex-1 border rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed"
      >
        <strong>{{ comment.display_name }}</strong>
        <span class="text-xs text-gray-400">{{
          $moment(comment.created_on).format('MMMM DD, YYYY hh:mm a')
        }}</span>
        <p class="text-sm">
          {{ comment.body }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import 'md5'
export default {
  components: {},
  props: {
    comment: {
      type: Object,
      required: true,
      default: () => {},
    },
  },
  data() {
    return {
      mailHash: '',
    }
  },
  computed: {
    getMailHash() {
      const hasher = require('md5')
      return hasher(this.comment.email.trim().toLowerCase())
    },
  },
}
</script>

// email.trim().toLowerCase()
