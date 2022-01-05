<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>Database homework</strong></router-link
        >
      </div>
    </nav>

    <div class="container">
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-8">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <article class="tile is-child notification is-primary">
                <p class="title">Restaurant</p>
                <div class="select is-primary">
                  <select v-model="selectedRestaurantId">
                    <option :value="null" v-if="selectedRestaurantId === null">
                      請選擇餐廳
                    </option>
                    <option
                      v-for="item in restaurants"
                      :key="item.rno"
                      :value="item.rno"
                    >
                      {{ item.rname }}
                    </option>
                  </select>
                </div>
              </article>
              <article class="tile is-child notification is-warning">
                <p class="title">Food</p>
                <div class="select is-primary">
                  <select v-model="selectedFoodId">
                    <option :value="null" v-if="selectedFoodId === null">
                      請選擇食物
                    </option>
                    <option
                      v-for="item in foods"
                      :key="item.fno"
                      :value="item.fno"
                    >
                      {{ item.fname }}
                    </option>
                  </select>
                </div>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child notification is-info">
                <p class="title">Middle tile</p>
                <p class="subtitle">With an image</p>
                <figure class="image is-4by3">
                  <img src="https://bulma.io/images/placeholders/640x480.png" />
                </figure>
              </article>
            </div>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-danger">
              <p class="title">Wide tile</p>
              <p class="subtitle">Aligned with the right tile</p>
              <div class="content">
                <!-- Content -->
              </div>
            </article>
          </div>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child notification is-success">
            <div class="content">
              <p class="title">Tall tile</p>
              <p class="subtitle">With even more content</p>
              <div class="content">
                <!-- Content -->
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>

    <div
      class="is-loading-bar has-text-centered"
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <footer class="footer">
      <p class="has-text-centered">Hi (c) 2022</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      restaurants: [],
      selectedRestaurantId: null,
      foods: [],
      selectedFoodId: null,
    };
  },
  mounted() {
    this.fetchRestaurant();
  },
  computed: {},
  watch: {
    selectedRestaurantId(newVal) {
      if (newVal) {
        this.selectedFoodId = null;
        this.foods = [];
        this.fetchFood();
      }
    },
  },
  methods: {
    async fetchRestaurant() {
      try {
        let res = await axios.get("/api/restaurants/");
        this.restaurants = res.data;
      } catch (e) {
        console.log(e);
      }
    },
    async fetchFood() {
      if (this.selectedRestaurantId === null) return;

      try {
        let res = await axios.get("/api/foods/", {
          params: {
            rno: this.selectedRestaurantId,
          },
        });
        this.foods = res.data;
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.container {
  margin: 20px, 0;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
