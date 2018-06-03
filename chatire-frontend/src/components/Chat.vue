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
        
        $.ajaxSetup({
            headers: {
                'Authorization': `Token ${sessionStorage.getItem('authToken')}`
            }
        })
        
        },

        methods: {
            startChatSession () {
                $.post('htttp://localhost:8000/api/chats/', (data)=> {
                    alert("A new session has been created you'll be redirected automatically")
                    this.sessionStarted = true
                    this.$router.push('/chats/chat_url')

                })
                .fail((response)=> {
                    alert(response.responseText)
                })
            }
        }
    }
</script>


<style scoped>
h1, h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

.btn {
    border-radius: 0;
}

.card-footer inputext[type="t"] {
    background-color: #ffffff;
    color: #444444;
    padding: 7px;
    font-size: 13px;
    border: 2px solid #cccccc;
    width: 100%;
    height: 30px;
}

.card-header a {
    text-decoration: underline;
}

.card-body {
    background-color: #ddd;
    margin-top: -15px;
    margin-bottom: -5px;
    height: 380px;
    overflow-y: auto;
}

.speech-bubble {
    display: inline-block;
    position: relative;
    border-radius: 0.4em;
    padding: 10px;
    background-color: #fff;
    font-size: 14px;
}

.subtle-blue-gradient {
    background: linear-gradient(45deg,#004bff, #007bff);
}

.speech-bubble-user:after {
    content: "";
    position: absolute;
    right: 4px;
    top: 10px;
    width: 0;
    height: 0;
    border: 20px solid transparent;
    border-left-color: #007bff;
    border-right: 0;
    border-top: 0;
    margin-top: -10px;
    margin-right: -20px;
}

.speech-bubble-peer:after {
    content: "";
    position: absolute;
    left: 3px;
    top: 10px;
    width: 0;
    height: 0;
    border: 20px solid transparent;
    border-right-color: #ffffff;
    border-top: 0;
    border-left: 0;
    margin-top: -10px;
    margin-left: -20px;
    
}

.chat-section:first-child {
    margin-top: 10px;
}

.chat-section {
    margin-top: 15px;
}

.send-section {
    margin-bottom: -20px;
    padding-bottom: 10px;
}




</style>

