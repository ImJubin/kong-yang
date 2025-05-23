import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";
import ArticleUpdateView from "@/views/ArticleUpdateView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/create",
      name: "create",
      component: ArticleCreateView,
    },
    {
      path: "/articles/:id/edit",
      name: "ArticleUpdateView",
      component: ArticleUpdateView,
    },
  ],
});

export default router;
