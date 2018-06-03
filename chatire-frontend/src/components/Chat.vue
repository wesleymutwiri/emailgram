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
                                    <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">Whatsup, another chat app?

                                    </span>
                                </div>
                                <div class="col-sm-2">
                                    <img src="http://placehold.it/40/f16000/fff&text=D" alt="" class="rounded-circle">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
