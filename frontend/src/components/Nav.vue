<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container">
            <button aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation"
                    class="navbar-toggler"
                    data-target="#navbarNav" data-toggle="collapse" type="button">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <a class="navbar-brand" href="/">Home</a>
                <a class="navbar-brand" href="/projects">Projects</a>
                <a class="navbar-brand" href="/ImageCaptions">Image Captions</a>
                <a class="navbar-brand" href="/login">Blog</a>
                <a class="navbar-brand">
                        <router-link class="nav-link" :to="{name:'about'}">About</router-link>
                </a>
                <ul class="navbar-nav mr-auto" v-if="loggedIn()">
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'my-posts'}">My Posts</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'new-post'}">New Post</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav mr-auto" v-else></ul>
                <ul class="navbar-nav my-2 my-lg-0" v-if="loggedIn()">
                    <li class="nav-item">
                        <a class="nav-link text-dark">{{userEmail}}</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:void(0)" v-on:click="logOut">Log Out</a>
                    </li>
                </ul>
                <ul class="navbar-nav my-2 my-lg-0" v-else hidden>
                    <li class="nav-item">
                        <router-link :to="{name: 'register'}" class="nav-link">Register</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{name: 'login'}" class="nav-link">Login</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        data () {
            return {
                message: 'test'
            }
        },
        name: "Nav",
        computed: {
            userEmail() {
                return localStorage.getItem('email')
            }
        },
        methods: {
            loggedIn() {
                return localStorage.getItem('loggedIn')
            },
            logOut() {
                localStorage.removeItem('actoken')
                localStorage.removeItem('loggedIn')
                localStorage.removeItem('email')
                this.$router.replace({name: 'login'})
                window.location.reload()
            }
        }
    }
</script>

<style scoped>

</style>