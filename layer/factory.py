import geopandas as gpd
from .layers import ReportLayer
from .layers import OverlapLayer
from .layers import NonOverlapLayer

from constants import (
    ARCGIS_STORAGE_FOLDER,
    WEBMAP_TITLE,
    REPORT_LAYER_NAME,
    OVERLAP_LAYER_NAME,
    NONOVERLAP_LAYER_NAME
)

class LayerFactory:
    def __init__(self, gis):
        self.gis = gis

    #TODO: Use dictionary instead of if-else soup
    #TODO: Figure out best way to pass 
    #TODO: Add cluster layer 
    #TODO: Add fast track layer

    def generate_layer(self, layer_name):
        if layer_name == REPORT_LAYER_NAME:
            layer_title = self._generate_title(REPORT_LAYER_NAME)
            return ReportLayer(
                self.gis, 
                layer_title,
                "Mapa de Costas-2024",
                None
            )
        
        elif layer_name == OVERLAP_LAYER_NAME:
            layer_title = self._generate_title(OVERLAP_LAYER_NAME)
            return OverlapLayer(
                self.gis, 
                layer_title,
                "Mapa de Costas-2024",
                "red"
            )

        elif layer_name == NONOVERLAP_LAYER_NAME:
            layer_title = self._generate_title(NONOVERLAP_LAYER_NAME)
            return NonOverlapLayer(
                self.gis, 
                layer_title,
                "Mapa de Costas-2024",
                "green"
            )

        else :
            raise Exception(f"{layer_name} not yet implemented!")

    #TODO: Add fast track layer
    #TODO: Add cluster layer
    def _generate_title(self, layer_name):
        TITLE_MAP = {
            REPORT_LAYER_NAME: "Observaciones",
            OVERLAP_LAYER_NAME: "Reservas Peligrando",
            NONOVERLAP_LAYER_NAME: "Reservas",
            
        }
        return TITLE_MAP[layer_name]