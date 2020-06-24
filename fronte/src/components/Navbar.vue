<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link
              :to="{ name: 'Home' }" 
              class="btn btn-secondary"
              >Home
            </router-link>
          </li>
          <li class="nav-item mx-1">
            <router-link 
              :to="{ name: 'branch-editor' }" 
              class="btn btn-secondary"
              >Add Branch
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>