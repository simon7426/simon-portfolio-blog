<script setup>
import { ref } from "vue";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";
import Vue3TagsInput from "vue3-tags-input";
import blogsService from "../services/blogs.service";
import SyncLoader from "vue-spinner/src/SyncLoader.vue";
import { useRouter } from "vue-router";

const props = defineProps({
  blog: {
    type: Object,
    required: false,
    default: () => ({
      id: "",
      title: "",
      body: "",
      tags: [],
    }),
  },
  pageTitle: {
    type: String,
    required: false,
    default: () => "Add Blog",
  },
});

const loadercolor = ref("#dcdde1");
const isLoading = ref(false);

const router = useRouter();

const id = ref(props.blog.id);
const title = ref(props.blog.title);
const text = ref(props.blog.body);
const tags = ref(props.blog.tags);
const button_value = ref(props.pageTitle.split(" ")[0]);

function handleChangeTag(t) {
  tags.value = t;
}

function routeToBlogsPage() {
  router.push({ name: "BlogsPage" });
}

function blogOperation() {
  const inp_title = title.value;
  const inp_text = text.value;
  const inp_tags = tags.value;
  if (inp_title !== "" && inp_text !== "") {
    isLoading.value = true;
    const blog = {
      title: inp_title,
      body: inp_text,
      tags: inp_tags,
    };
    if (button_value.value == "Add") {
      blogsService.add_blog(blog).then(() => {
        routeToBlogsPage();
      });
    } else if (button_value.value == "Edit") {
      blogsService.edit_blog(id.value, blog).then(() => {
        routeToBlogsPage();
      });
    }
  }
}
</script>
<template>
  <div class="flex flex-col items-center px-6 py-12 h-4/5">
    <div class="w-3/4">
      <label
        class="block text-gray-700 text-center text-lg font-bold mb-2"
        for="title"
      >
        {{ pageTitle }}
      </label>
    </div>
    <div class="w-3/4">
      <div class="py-2">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
          Title
        </label>
        <input
          v-model="title"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          placeholder="Title"
        />
      </div>
      <div class="py-2">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="username"
        >
          Body
        </label>
        <md-editor
          v-model="text"
          :language="'en-US'"
          :toolbarsExclude="['github']"
        />
      </div>
      <div class="py-2">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
          Tags
        </label>
        <div>
          <vue3-tags-input
            :tags="tags"
            placeholder="input tags"
            @on-tags-changed="handleChangeTag"
          />
        </div>
      </div>
      <div class="flex justify-end">
        <div
          class="w-32 py-2.5 px-2.5 text-sm font-medium text-center text-white focus:outline-none bg-secondary rounded-full grey-button-bg focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
        >
          <button
            @click="blogOperation"
            type="button"
            data-mdb-ripple="true"
            data-mdb-ripple-color="light"
            :disabled="isLoading"
          >
            <SyncLoader :loading="isLoading" :color="loadercolor" />
            <p v-if="!isLoading">{{ button_value }}</p>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
.v3ti .v3ti-tag {
  background: $secondary;
  /*border: 1px solid #222222;*/
  /*border-radius: 0;*/
}

.v3ti .v3ti-tag .v3ti-remove-tag {
  color: #000000;
  transition: color 0.3s;
}

.v3ti .v3ti-tag .v3ti-remove-tag:hover {
  color: red;
}

.grey-button-bg:hover {
  background-color: $secondarylight;
  cursor: pointer;
}
</style>
