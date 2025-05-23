import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import MyPageView from '@/views/MyPageView.vue'
import UpdateMyDataView from '@/views/UpdateMyDataView.vue' 

// ✅ 로그인된 사용자가 회원가입 페이지에 접근하지 못하도록
const requireNotLoggedIn = (to, from, next) => {
  const token = localStorage.getItem('token')
  if (token) {
    next('/') // 홈으로 리다이렉트
  } else {
    next()
  }
}
// 로그인 되지 않은 사용자가 회원제 페이지에 들어가려고 할 때때
const requireLoggedIn = (to, from, next) => {
  const token = localStorage.getItem('token')
  if (!token) {
    next({ name: 'Login' })
  } else {
    next()
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/users/signup',
      name: 'SignUp',
      component: SignUpView,
      beforeEnter: requireNotLoggedIn  // ✅ 로그인 상태 체크
    },
    {
      path: '/users/login',
      name: 'Login',
      component: LoginView,
      beforeEnter: requireNotLoggedIn
    },
    {
      path: '/users/mypage',
      name: 'MyPage',
      component: MyPageView,
      beforeEnter: requireLoggedIn
    },
    {
      path: '/users/update',
      name: 'UpdateMyData',
      component: UpdateMyDataView,
      beforeEnter: requireLoggedIn
    }
  ],
})

export default router
