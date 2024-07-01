<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
import { ref, watch } from 'vue'

// county: 시(도) , city: 자치구 (시), bank : 은행 
const props = defineProps({
  county: String,
  city: String,
  bank: String,
})

const map = ref();
const markerList = ref([]);
const triggerSearch = ref(false); // search 트리거 값

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  searchPlaces();
};

const searchPlaces = () => {
  if (!props.county || !props.city || !props.bank) {
    return;
  }

  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places();
  // 키워드로 장소를 검색합니다
  ps.keywordSearch(`${props.county} ${props.city} ${props.bank}`, placesSearchCB);
}

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    const bounds = new kakao.maps.LatLngBounds();
    markerList.value = [];

    for (let marker of data) {
      const markerItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: marker.place_name,
          visible: false
        }
      };
      markerList.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.value?.setBounds(bounds);
  }
};

// 마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다
const onClickMapMarker = (markerItem) => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};

// props 및 트리거가 변경될 때마다 장소 검색을 수행합니다
watch([() => props.county, () => props.city, () => props.bank, triggerSearch], searchPlaces);
</script>

<template>
  <div class="map">
    <KakaoMap :lat="37.566826" :lng="126.9786567" @onLoadKakaoMap="onLoadKakaoMap">
      <KakaoMapMarker
        v-for="(marker, index) in markerList"
        :key="index"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @onClickKakaoMapMarker="onClickMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>

<style scoped>
.map {
  width: 100%;
  height: 100%;
}
</style>
