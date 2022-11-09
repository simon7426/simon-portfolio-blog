<template>
  <div>
    <div class="flex mx-auto items-center justify-center pb-2">
      <div class="w-full bg-white rounded-lg px-2 pt-2">
        <div class="flex flex-wrap -mx-3 mb-6">
          <h2 class="mb-4 text-lg font-semibold text-gray-900">
            Add a comment
          </h2>
          <div class="flex items-end w-full md:w-full pl-2 mb-2 mt-2">
            <div class="mb-4 pr-2">
              <input
                id="username"
                v-model="displayName"
                class="bg-gray-100 rounded border border-gray-400 leading-normal resize-none py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white"
                type="text"
                placeholder="Username"
              />
            </div>
            <div class="mb-4">
              <input
                id="hello"
                v-model="email"
                class="bg-gray-100 rounded border border-gray-400 leading-normal resize-none py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white"
                type="text"
                placeholder="Email"
              />
            </div>
          </div>
          <div class="w-full md:w-full pl-2 mb-2 mt-2">
            <textarea
              id="body"
              v-model="body"
              class="bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-28 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white"
              name="body"
              placeholder="Type Your Comment"
              required
            ></textarea>
          </div>
          <div class="w-full md:w-full flex items-end">
            <div class="ml-auto">
              <button
                class="bg-transparent hover:bg-gray-500 text-gray-700 font-semibold hover:text-white py-2 px-4 border border-gray-500 hover:border-transparent rounded"
                @click="onSubmit"
              >
                Submit
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ErrorModal v-show="errorModal" @close-modal="errorModal = false" />
  </div>
</template>

<script>
import ErrorModal from './errorModal.vue'
export default {
  components: { ErrorModal },
  props: {
    blogid: {
      type: String,
      required: true,
      default: () => '',
    },
  },
  data() {
    return {
      email: '',
      displayName: '',
      body: '',
      errorModal: false,
    }
  },
  methods: {
    validateInputs() {
      if (
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          this.email
        )
      ) {
        return true
      } else {
        return false
      }
    },
    async onSubmit() {
      if (this.validateInputs()) {
        if (process.client) {
          const token = await this.$recaptcha.execute('comment')
          this.$axios.setHeader('X-Recaptcha-Key', token)
        }
        const ret = await this.$axios
          .post(`/api/v1/blogs/${this.$props.blogid}/comment`, {
            email: this.email,
            display_name: this.displayName,
            body: this.body,
          })
          .then((response) => {
            return response.data
          })
        this.email = ''
        this.displayName = ''
        this.body = ''
        this.$emit('comment-added', ret)
      } else {
        this.errorModal = true
      }
    },
  },
}
</script>
