<template>
<div class="container">
    <h1 class="text-center">Welcome to Where'sUp</h1>
    <div id="auth-container" class="row">
        <div class="col-sm-4 offset-sm-4" >
            <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
                <li class="nav-item">
                    <a href="#signup" class="nav-link active" data-toggle="tab" role="tab" aria-controls="signup" aria-selected="true">Sign Up</a>
                </li>
                <li class="nav-item">
                    <a href="#signin" class="nav-link" id="signin-tab" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
                </li>
            </ul>
            <div class="tab-content" id="myTabContent">
                <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="sigin-tab"></div>
                <form @submit.prevent="signUp">
                    <div class="form-group">
                        <input type="email" v-model="email" id="email" class="form-control" placeholder="Email Address" required>
                    </div>
                    <div class="form-row">
                        <div class="form-group col-md-6">
                            <input type="text" v-model="username" id="username" class="form-control" placeholder="Username" required>
                        </div>
                        <div class="form-group col-md-6">
                            <input type="password" v-model="password" id="password" class="form-control">
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>