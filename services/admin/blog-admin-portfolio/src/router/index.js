import { createRouter, createWebHistory } from "vue-router";
import tokenService from "../services/token.service";
import LoginPage from "../pages/LoginPage.vue";
import DashboardPage from "../pages/DashboardPage.vue";
import BlogsPage from "../pages/BlogsPage.vue";
import AddBlog from "../pages/AddBlog.vue";
import EditBlog from "../pages/EditBlog.vue";
const routes = [
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
    meta: {
      requireAuth: false,
    },
  },
  {
    path: "/",
    name: "DashboardPage",
    component: DashboardPage,
    meta: {
      requireAuth: true,
    },
  },
  {
    path: "/blogs",
    name: "BlogsPage",
    component: BlogsPage,
    meta: {
      requireAuth: true,
    },
  },
  {
    path: "/add-blog",
    name: "AddBlog",
    component: AddBlog,
    meta: {
      requireAuth: true,
    },
  },
  {
    path: "/edit-blog/:blogid",
    name: "EditBlog",
    component: EditBlog,
    meta: {
      requireAuth: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requireAuth)) {
    const user = tokenService.getUser();
    if (user === null) {
      next({ name: "LoginPage" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
