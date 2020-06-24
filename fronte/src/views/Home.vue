<template>
  <div class="home">
    <div class="container">
      <div class="row">    
        <h1>Branch List</h1>   
        <table class="table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th >Branch_name</th>
                    <th>Address</th>
                    <th>Organisation</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr div v-for="branchs in branch"
                      :key="branchs.pk"  @delete-branchs="deleteBranch">
                    <th scope="row">{{branchs.id}}</th>
                    <!-- <td>{{branchs.branch_name}}</td> -->
                     <td><router-link
            :to="{ name: 'branch', params: { id: branchs.id } }"
            class="branch-link"
            >{{branchs.branch_name}}
          </router-link></td>
                    <td>{{branchs.address}}</td>
                    <td>{{branchs.org}}</td>
                    
                    <td>
                      <router-link :to="{ name: 'questiom-editor' }" class='btn btn-sm btn-danger'>Edit</router-link>
                      <button
                              class="btn btn-sm btn-outline-danger"
                              @click="triggerDeleteBranch"
                              >Delete
                            </button>
                      <!-- <button class="btn btn-sm btn-outline-success" v-on:click="getBranch(branchs.id)">Edit</button>
                      <button class="btn btn-sm btn-danger" v-on:click="deleteBranch(branchs.id)">Delete</button> -->
                    </td>
                  </tr>
                </tbody>
          </table>
      </div>
      <div class="my-4">
        <p v-show="loadingBranch">...loading...</p>
        <button
          v-show="next"
          @click="getBranch"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </div>

  
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      branch: [],
      next: null,
      loadingBranch: false,
      requestUser: null
    }
  },
  methods: {
    getBranch() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/branch/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingBranch = true;
      apiService(endpoint)
        .then(data => {
          this.branch.push(...data.results)
          this.loadingBranch = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    async deleteBranch(branchs) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/api/branch/${branchs.id}/`;
      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.branch, this.branch.indexOf(branchs))
      }
      catch (err) {
        console.log(err)
      }
    },
    triggerDeleteBranch() {
      // emit an event to delete an answer instance
      this.$emit("delete-branchs", this.branchs)
    }
    
  },
  created() {
    this.getBranch()
    this.setRequestUser()
    document.title = "Branch List";
  },
 
};
</script>
<style scoped>
table{
 width:100%
}
thead{
  background-color: #4CAF50;
 
}
th,td{
  border:1px solid gray;
 
}
.branch-link {
  font-weight: bold;
  color: black;
}

.branch-link:hover {
  color: #30475e;
  text-decoration: none;
}

</style>

