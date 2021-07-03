<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      Hi! My name is Adam Weinberger, and I am a data scientist in the DC area. I have worked on dozens of data science projects professionally, personally, and academically. Some topics that I am especially interested in are:
      <br>
      <ul>
        <li>AI / Machine Learning</li><br>
        <li>Economics</li><br>
        <li>Sports</li><br>
      </ul>
    </p>
    <p>{{ message }}</p>
    <button v-on:click="reverseMessage">Reverse Message</button>
    
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
    reverseMessage() {
      this.message = this.message.split('').reverse().join('')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
