package com.SAR_Generator.main_service.services;

import com.SAR_Generator.main_service.dto.AlertDTO;

import java.util.List;

public interface AlertService {
    public List<AlertDTO> getAlerts();
}
