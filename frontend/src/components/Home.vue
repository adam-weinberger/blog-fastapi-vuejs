<template>
  <div>
    <div class="float-child">
      Hi! My name is Adam Weinberger, and I am a data scientist in the DC area. I have worked on dozens of data science projects professionally, personally, and academically. Some topics that I am especially interested in are:
      <br>
      <br>
      <ul>
        <li>Machine learning</li>
        <li>Economics</li>
        <li>Sports</li>
        <li>Traveling</li>
      </ul>
    </div>
    <div class="float-child">
      <img src="../assets/bangkok_temple.jpeg" alt="picture here" width="100%">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'This is a message'
    }
  },
  name: 'About',
  props: {
    msg: String
  },
  methods: {
    async testConnection() {
      try {
        await this.axios.get('/posts/test').then(response => {
                this.posts = response.data
            })
      } catch (err) {
        console.log(err)
    }
    }
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
