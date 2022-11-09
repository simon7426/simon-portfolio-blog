import api from "./api";

class BlogService {
  async get_blogs() {
    return api.get("/blogs").then((response) => {
      return response.data;
    });
  }
  async add_blog({ title, body, tags }) {
    return api
      .post("/blogs", {
        title,
        body,
        tags,
      })
      .then((response) => {
        return response.data;
      });
  }
  async get_blog(blog_id) {
    return api.get(`/blogs/${blog_id}`).then((response) => {
      return response.data;
    });
  }
  async edit_blog(blog_id, { title, body, tags }) {
    return api
      .put(`/blogs/${blog_id}`, {
        title,
        body,
        tags,
      })
      .then((response) => {
        return response.data;
      });
  }
  async delete_blog(blog_id) {
    return api.delete(`/blogs/${blog_id}`).then((response) => {
      return response.status;
    });
  }
}

export default new BlogService();
