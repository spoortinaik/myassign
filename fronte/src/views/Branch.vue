<template>
     <div class="single-question mt-2">
    <div v-if="question" class="container">
    </div>
     <h1 style="color:green">{{ branch.branch_name }}</h1>
    <center><p  class="branch-name">{{ branch.address }}</p> </center>
    </div>
    
</template>



<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Branch",
  props: {
    id:{
      type: String,
      required: true
    }
  },
  data() {
    return {
      branch: [],
      next: null,
    }
  },
  methods: {
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    
    getBranchData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/branch/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.branch = data;
            this.userHasAnswered = data.user_has_answered;
            this.setPageTitle(data.branch_name)
          } else {
            this.branch = null;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    }
    
  },
  created() {
    this.getBranchData()

  }
  
}
</script>
<style scoped>
.branch-name {
  width: 100%;
  border: 5px solid black;
  padding: 50px;
  margin: 20px;
}


</style>


