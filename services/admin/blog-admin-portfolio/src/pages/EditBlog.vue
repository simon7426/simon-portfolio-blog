<script setup>
import blogsService from "../services/blogs.service";
import LoaderGrid from "../components/LoaderGrid.vue";
import { ref } from "vue";
import { useRoute } from "vue-router";
import BlogModify from "../components/BlogModify.vue";
const route = useRoute();
const blogid = route.params.blogid;

const isLoadingComplete = ref(false);

const blog = ref({});

async function loadBlog() {
  await blogsService.get_blog(blogid).then((data) => {
    blog.value.id = data._id;
    blog.value.title = data.title;
    blog.value.body = data.body;
    blog.value.tags = data.tags;
    isLoadingComplete.value = true;
  });
}
loadBlog();
</script>
<template>
  <LoaderGrid v-if="!isLoadingComplete" />
  <BlogModify v-if="isLoadingComplete" :blog="blog" page-title="Edit Page" />
</template>
