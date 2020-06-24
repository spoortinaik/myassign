<template>
  <div class="container mt-2">
    <h1 class="mb-3">Add branch</h1>
    <form @submit.prevent="onSubmit">
      <input type="text" class="form-control" v-model="branch_name" placeholder="enter Branch">
      <br>
      <textarea
        v-model="branch_address"
        class="form-control"
        placeholder="enter address?"
        rows="3"
      ></textarea>
      <br>
      <select  class="form-control" v-model="branch_org" >
        <option v-for="orgs in org" :value="orgs.id" :key="orgs.id">{{orgs.org_name}}</option>
        </select>
      <br>
      <button
        type="submit"
        class="btn btn-success"
        >Add Branch
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "branch-editor",
  props: {
    id: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      branch_name:null,
      branch_address: null,
      branch_org:null,
      error: null,
      org:null,
    }
  },
  methods: {

     getOrg() {
      let endpoint = "/api/org/";
      if (this.next) {
        endpoint = this.next;
      }
      apiService(endpoint).then(org => {
        this.org = org.results;    
          })  

    },
    onSubmit() {
      // Tell the REST API to create or update a Branch Instance
      if (!this.branch_name) {
        this.error = "You need to add branch name";
      }  
      else {
        let endpoint = "/api/branch/";
        let method = "POST";  
        apiService(endpoint, method, {
          "branch_name": this.branch_name,
          "address": this.branch_address,
          "org":this.branch_org.id
          
          })
          .then(branch_data => {
             this.$router.push({ 
              name: 'Home', 
              params: { id: branch_data.id }
            });   
          })  
      }
    },
    
  },

  created() {
    this.getOrg();
    this.onSubmit();
    document.title = "Add branch";
    console.log(this.branch_org); 
  }  
}
</script>