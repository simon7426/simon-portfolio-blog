<template>
  <div class="container w-full md:max-w-3xl mx-auto pt-10">
    <div
      class="w-full px-4 md:px-6 text-xl text-gray-800 leading-normal"
      style="font-family: Georgia, serif"
    >
      <div class="font-sans">
        <p class="text-base md:text-sm text-green-500 font-bold">
          &lt;
          <NuxtLink
            to="/"
            class="text-base md:text-sm text-green-500 font-bold no-underline hover:underline"
            >BACK TO BLOG</NuxtLink
          >
        </p>
        <h1
          class="font-bold font-sans break-normal text-gray-900 pt-6 pb-2 text-3xl md:text-4xl"
        >
          {{ post.title }}
        </h1>
        <p class="text-sm md:text-base font-normal text-gray-600">
          Published {{ $moment(post.createdAt).format('MMMM DD, YYYY') }}
        </p>
      </div>
      <hr />
    </div>

    <!-- <p >{{ post.body }}</p> -->
    <BlogBody class="px-4 py-6" :body="post.body" />

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
    <AuthorCard />
    <AddCommentCard :blogid="post._id" @comment-added="postComment" />
    <CommentListCard v-if="getComments" :comments="getComments" />
  </div>
</template>

<script>
import AuthorCard from './AuthorCard.vue'
import CommentListCard from './CommentListCard.vue'
import AddCommentCard from './AddCommentCard.vue'
import BlogBody from './BlogBody.vue'
export default {
  components: { AuthorCard, CommentListCard, AddCommentCard, BlogBody },
  props: {
    post: {
      type: Object,
      required: true,
      default: () => {},
    },
  },
  data() {
    return {
      comments: this.post.comments,
      body: this.post.body,
    }
  },
  head() {
    return {
      title: this.post.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.post.title,
        },
        {
          hid: 'keywords',
          name: 'keywords',
          content: this.post.tags.join(', '),
        },
        {
          hid: 'author',
          name: 'author',
          content: 'Simon Islam',
        },
      ],
    }
  },
  computed: {
    getComments() {
      return this.comments
    },
  },
  methods: {
    postComment(ret) {
      this.comments = ret.comments
    },
  },
}
</script>
