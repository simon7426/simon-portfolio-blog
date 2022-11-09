<template lang="md">
    <div id="md" v-html="$md.render(body)"></div>
</template>
<script>
export default {
  components: {},
  props: {
    body: {
      type: String,
      required: true,
      default: () => {},
    },
  },
}
</script>
<style>
#md ol {
  list-style-type: number;
  @apply ml-8;
}

#md h1,
#md h2,
#md h3,
#md h4,
#md h5,
#md h6,
#md p {
  @apply mb-1;
}

#md section {
  @apply mb-4;
}
</style>
