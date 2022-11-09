<script setup>
import { ref } from "vue";
import blogService from "../services/blogs.service";
import PencilIcon from "vue-material-design-icons/Pencil.vue";
import PlusIcon from "vue-material-design-icons/Plus.vue";
import DeleteIcon from "vue-material-design-icons/Delete.vue";
import CheckIcon from "vue-material-design-icons/Check.vue";
import CloseIcon from "vue-material-design-icons/Close.vue";
import moment from "moment-timezone";
import { useRouter } from "vue-router";
import LoaderGrid from "./LoaderGrid.vue";

const blogs = ref([]);
const router = useRouter();
const isLoadingComplete = ref(false);
const clickedData = ref({});
const isDisabled = ref(false);

function deleteClick(blogid) {
  clickedData.value[blogid] = !clickedData.value[blogid];
  isDisabled.value = !isDisabled.value;
}

function getDisabled(blogid) {
  return isDisabled.value && !clickedData.value[blogid];
}

function deleteFromBlogs(blogid) {
  for (let i = 0; i < blogs.value.length; i++) {
    if (blogs.value[i]["_id"] == blogid) {
      blogs.value.splice(blogs.value.indexOf(blogs.value[i]), 1);
    }
  }
  isDisabled.value = !isDisabled.value;
}

function dateTime(time) {
  return moment.tz(time, "UTC").clone().tz("Asia/Dhaka").format("LLL");
}

function checkClickHandler(blogid) {
  if (clickedData.value[blogid] === false) {
    editBlog(blogid);
  } else {
    deleteBlog(blogid);
  }
}

function editBlog(blogid) {
  router.push({
    name: "EditBlog",
    params: {
      blogid: blogid,
    },
  });
}

function deleteBlog(blogid) {
  blogService.delete_blog(blogid).then(() => {
    deleteFromBlogs(blogid);
  });
}

async function getAllBlogs() {
  await blogService
    .get_blogs()
    .then((response) => {
      blogs.value = response;
      isLoadingComplete.value = true;
    })
    .then(() => {
      for (let i = 0; i < blogs.value.length; i++) {
        clickedData.value[blogs.value[i]["_id"]] = false;
      }
    })
    .catch(() => {
      // console.log(err.message);
    });
}

getAllBlogs();
</script>

<template>
  <LoaderGrid v-if="!isLoadingComplete" />
  <div
    v-if="isLoadingComplete"
    class="flex flex-col items-center px-6 py-12 h-4/5"
  >
    <div class="w-3/4 flex justify-end">
      <router-link to="/add-blog">
        <div
          class="w-32 flex flex-row justify-between py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-transparent rounded-full hover:bg-gray-100 hover:text-black-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
        >
          <PlusIcon :size="20" />
          Add Blog
        </div>
      </router-link>
    </div>

    <div
      class="w-3/4 justify-center overflow-x-auto relative shadow-md sm:rounded-lg"
    >
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead
          class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
        >
          <tr>
            <th scope="col" class="py-3 px-6 text-center">Created At</th>
            <th scope="col" class="py-3 px-6 text-center">Title</th>
            <th scope="col" class="py-3 px-6 text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" :key="blog._id" class="bg-white border-b">
            <td class="py-2 px-6 text-center">
              {{ dateTime(blog.created_at) }}
            </td>
            <th
              scope="row"
              class="py-2 px-6 font-medium text-gray-900 whitespace-nowrap text-center dark:text-white"
            >
              {{ blog.title }}
            </th>
            <td class="py-2 px-6 text-center">
              <div class="flex flex-row justify-center">
                <button
                  :disabled="getDisabled(blog._id)"
                  @click="checkClickHandler(blog._id)"
                  class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-full border border-gray-200 enabled:hover:bg-gray-100 enabled:hover:text-green-700 focus:z-10 focus:ring-0 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 disabled:opacity-60"
                >
                  <PencilIcon v-if="!clickedData[blog._id]" />
                  <CheckIcon v-if="clickedData[blog._id]" />
                </button>
                <button
                  :disabled="getDisabled(blog._id)"
                  @click="deleteClick(blog._id)"
                  class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium shadow-none text-gray-900 focus:outline-none bg-white rounded-full border border-gray-200 enabled:hover:bg-gray-100 enabled:hover:text-red-700 focus:z-10 focus:ring-0 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 disabled:opacity-60"
                >
                  <DeleteIcon v-if="!clickedData[blog._id]" />
                  <CloseIcon v-if="clickedData[blog._id]" />
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
