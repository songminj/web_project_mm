<template>
  <div class="container">
    <h1>예금 상품 정보 및 그래프</h1>
    <div v-if="deposits.length === 0" class="no-deposits">
      등록된 예금 상품이 없습니다.
    </div>
    <div v-else>
      <div v-for="(item, index) in deposits" :key="index" class="product-card">
        <h2>{{ item.product.fin_prdt_nm }} ({{ item.product.kor_co_nm }})</h2>
        <div class="product-details">
          <img :src="'data:image/png;base64,' + item.graph" alt="Graph" class="graph" v-if="item.graph">
          <div class="details">
            <p><strong>상품명:</strong> {{ item.product.fin_prdt_nm }}</p>
            <p><strong>은행명:</strong> {{ item.product.kor_co_nm }}</p>
            <p><strong>가입 방법:</strong> {{ item.product.join_way }}</p>
            <p><strong>특별 조건:</strong> {{ item.product.spcl_cnd }}</p>
            <p><strong>가입 거부:</strong> {{ item.product.join_deny }}</p>
            <p><strong>가입 대상:</strong> {{ item.product.join_member }}</p>
            <p><strong>최대 한도:</strong> {{ item.product.max_limit }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const store = useCounterStore();
    const deposits = ref([]);

    onMounted(async () => {
      const depositData = await store.getMyDeposit();
      const graphData = await store.getDepositGraphs();

      // Ensure depositData and graphData are arrays
      if (Array.isArray(depositData) && Array.isArray(graphData)) {
        // Map graph data to the corresponding deposit
        depositData.forEach(deposit => {
          const graph = graphData.find(graph => graph.product_name === deposit.product.fin_prdt_nm);
          if (graph) {
            deposit.graph = graph.graph;
          }
        });

        deposits.value = depositData;
      } else {
      }
    });

    return {
      deposits
    };
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #0056b3;
}

.no-deposits {
  text-align: center;
  font-size: 18px;
  color: #888;
}

.product-card {
  border: 1px solid #0056b3;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.product-card h2 {
  margin-top: 0;
  color: #0056b3;
}

.product-details {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.graph {
  max-width: 300px;
  margin-right: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.details {
  flex: 1;
}

.details p {
  margin: 8px 0;
}

.details strong {
  display: inline-block;
  width: 100px;
  color: #333;
}

@media (max-width: 768px) {
  .product-details {
    flex-direction: column;
    align-items: flex-start;
  }

  .graph {
    margin-right: 0;
    margin-bottom: 20px;
    width: 100%;
  }
}
</style>
