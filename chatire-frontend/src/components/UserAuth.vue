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
                            <input type="password" v-model="password" id="password" class="form-control" placeholder="Password" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="toc" required>
                            <label for="gridCheck" class="form-check-label">
                            Accept terms and Conditions
                            </label>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-block btn-primary">Sign Up</button>
                </form>
            </div>
            <div class="tab-pane fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
                <form @submit.prevent="signin">
                    <div class="form-group">
                        <input type="text" v-model="username" id="username" class="form-control" placeholder="Username" required>

                    </div>
                    <div class="form-group">
                        <input type="password" v-model="password" id="password" class="form-control" placeholder="PAssword" required>
                    </div>
                    <button type="submit" class="btn btn-block btn-primary"> Sign In </button>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    const $ = window.jQuery

export default {

    data() {
        return {
            email: '', username: '', password: ''
            }
        }
    }
</script>
<style scoped>
#auth-container{
    margin-top: 50px;
}
.tab-content {
    padding-top: 20px;
}
</style>
