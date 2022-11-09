<template>
  <div>
    <h3 class="mb-4 text-lg font-semibold text-gray-900">Comments</h3>
    <CommentCard
      v-for="comment in comments"
      :key="comment._id"
      :comment="comment"
    />
  </div>
</template>

<script>
export default {
  components: {},
  props: {
    comments: {
      type: Array,
      required: true,
      default: () => {},
    },
  },
}
</script>
