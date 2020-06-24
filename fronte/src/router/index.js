import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Branch from "../views/Branch.vue";
import BranchEditor from "../views/BranchEditor.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },

  {
    // the ? sign makes the slug parameter optional
    path: "/branch/:id",
    name: "branch",
    component: Branch,
    props: true,
  },

  {
    // the ? sign makes the slug parameter optional
    path: "/add",
    name: "branch-editor",
    component: BranchEditor,
    props: true,
  },


  
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
