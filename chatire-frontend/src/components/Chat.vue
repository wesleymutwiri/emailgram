<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-6 offset-3">
                <div v-if="sessionStarted" class="card" id="chat-container">
                    <div class="card-header text-white text-center font-weight-bold subtle-blue-gradient">
                        Share the page URL to invite new friends
                    </div>
                    <div class="card-body">
                        <div class="container chat-body">
                            <div class="row chat-section">
                                <div class="col-sm-2">
                                    <img src="http://placehold.it/40/f16000/fff&text=D" alt="" class="rounded-circle">
                                </div>
                                <div class="col-sm-7">
                                    <span class="card-text speech-bubble speech-bubble-peer">Hello!</span>
                                </div>
                            </div>
                            <div class="row chat-section">
                                <div class="col-sm-7 offset-3">
                                    <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                                        Whatsup, another chat app?

                                    </span>
                                </div>
                                <div class="col-sm-2">
                                    <img src="http://placehold.it/40/f16000/fff&text=D" alt="" class="rounded-circle">
                                </div>
                            </div>
                            <div class="row chat-section">
                                <div class="col-sm-2">
                                    <img src="http://placehold.it/40/f16000/fff&text=D" alt="" class="rounded-circle">
                                </div>
                                <div class="col-sm-7">
                                    <p class="card-text speech-bubble speech-bubble-peer">
                                        Yes this is Emailgram, It's a pretty cool app that is open source an it was built using Django and Vue Js 
                                    </p>
                                </div>
                            </div>
                            <div class="row chat-section">
                                <div class="col-sm-7 offset-3">
                                    <p class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                                        Welcome 
                                    </p>
                                </div>
                                <div class="col-sm-2">
                                    <img src="http://placehold.it/40/f16000/fff&text=D" alt="" class="rounded-circle">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer text-muted">
                        <form>
                            <div class="row">
                                <div class="col-sm-10">
                                    <input type="text" placeholder="Type a message">
                                </div>
                                <div class="col-sm-2">
                                    <button class="btn btn-primary">Send</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div v-else>
                    <h3 class="text-center">
                        Welcome
                    </h3>
                    <br>
                    <p class="text-center">
                        To start chatting with friends click on the button below and start a new chat session and then you can invite friends over to chat
                    </p>
                    <br>
                    <button @click="startChatSession" class="btn btn-primary btn-lg btn-block">
                        Start Chatting
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    const $ = window.jQuery

    export default {
        data () {
            return {
                sessionStarted: false
            }
        },
        created () {
            this.username = sessionStorage.getItem('username')
        },
        methods: {
            startChatSession () {
                this.sessionStarted = true
                this.$router.push('/chats/chat_url')
            }
        }
    }
</script>
