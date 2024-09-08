<template>
    <div id="app">
        <div class="header-container">
            <h1>Africa CSIRTs Map</h1>
            <RouterLink :to="{ name: 'add' }" class="button-green">Add new CSIRT</RouterLink>
        </div>
        <div class="search-filter">
            <input v-model="searchQuery" placeholder="Search for a CSIRT...">
        </div>
        <div id="map-container"></div>
    </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import 'ol/ol.css';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { Feature } from 'ol';
import { Point } from 'ol/geom';
import { fromLonLat } from 'ol/proj';
import { Vector as VectorLayer } from 'ol/layer';
import { Vector as VectorSource } from 'ol/source';
import { Style, Icon } from 'ol/style';
import { fetchCSIRTs, updateCSIRT as updateCSIRTApi, addCSIRT as addCSIRTApi } from '../services/api.js';

export default {
    name: 'App',
    setup() {
        const csirts = ref([]);
        const searchQuery = ref('');
        const map = ref(null);

        const filteredCSIRTs = computed(() => {
            return csirts.value.filter(csirt =>
                csirt.name.toLowerCase().includes(searchQuery.value.toLowerCase())
            );
        });

        const loadCSIRTs = async () => {
            try {
                csirts.value = await fetchCSIRTs();
                updateMap();
            } catch (error) {
                console.error('Error fetching CSIRTs:', error);
            }
        };

        const updateMap = (list = null) => {
            if (map.value) {
                const vectorSource = new VectorSource();
                if (list) csirts.value = list;
                csirts.value.forEach(csirt => {
                    const feature = new Feature({
                        geometry: new Point(fromLonLat([csirt.longitude, csirt.latitude])),
                    });
                    feature.setStyle(
                        new Style({
                            image: new Icon({
                                anchor: [0.5, 1],
                                src: 'https://openlayers.org/en/latest/examples/data/icon.png',
                            }),
                        })
                    );
                    vectorSource.addFeature(feature);
                });

                const vectorLayer = new VectorLayer({
                    source: vectorSource,
                });


                map.value.getLayers().forEach(layer => {
                    if (layer instanceof VectorLayer) {
                        map.value.removeLayer(layer);
                    }
                });

                map.value.addLayer(vectorLayer);
            }
        };

        const updateCSIRT = async (updatedCSIRT) => {
            try {
                const result = await updateCSIRTApi(updatedCSIRT);
                const index = csirts.value.findIndex(c => c.id === result.id);
                if (index !== -1) {
                    csirts.value[index] = result;
                }
                updateMap();
            } catch (error) {
                console.error('Error updating CSIRT:', error);
            }
        };

        const addCSIRT = async (newCSIRT) => {
            try {
                const result = await addCSIRTApi(newCSIRT);
                csirts.value.push(result);
                updateMap();
            } catch (error) {
                console.error('Error adding CSIRT:', error);
            }
        };

        watch(searchQuery, () => {
            const result = csirts.value.filter(csirt => {
                return csirt.name.toLowerCase().includes(searchQuery.value.toLowerCase())
            }
            );
            updateMap(result);
        });


        onMounted(() => {
            map.value = new Map({
                target: 'map-container',
                layers: [
                    new TileLayer({
                        source: new OSM(),
                    }),
                ],
                view: new View({
                    center: fromLonLat([10, 0]),
                    zoom: 3,
                    projection: 'EPSG:3857',
                }),
            });
            loadCSIRTs();
        });

        return {
            csirts,
            searchQuery,
            filteredCSIRTs,
            updateCSIRT,
            addCSIRT,
        };
    },
};
</script>

<style>
#app {
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

#map-container {
    height: 500px;
    margin-bottom: 20px;
}

.search-filter {
    margin-bottom: 20px;
}

input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
}

.button-green {
    background-color: #28a745;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

.button-green:hover {
    background-color: #218838;
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>