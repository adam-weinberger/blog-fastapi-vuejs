<template>
  <div>
    <div>
      <button v-on:click="testConnection">Test</button> 
      {{ connectionMessage }}
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
        <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pictureMessage: 'Me, in Bangkok in 2018',
      connectionMessage: 'Not connected',
      file: '',
    }
  },
  name: 'ImageCaptions',
  props: {
    msg: String
  },
  methods: {
    async testConnection() {
      try {
        await this.axios.get('/users/test').then(response => {
                this.connectionMessage = response.data
            })
      } catch (err) {
        console.log(err)
      }
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },
    submitFile(){
      let formData = new FormData()
      formData.append('file', this.file)

      this.axios.post( '/users/single-file',
          formData,
          {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
          }
        ).then(result => {
          console.log('result ', result);
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        })

    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Container holding the image and the text */
.container {
  position: absolute;
}

.left-text{
	float: left;
}

.right-picture{
	float: right;
}

.float-child {
    width: 50%;
    float: left;
    padding: 10px;
} 

h3 {
  margin: 40px 0 0;
}
ul {
  padding: 0;
}
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
