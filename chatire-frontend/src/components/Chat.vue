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

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
