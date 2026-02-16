package com.SAR_Generator.main_service.dto;

import java.time.OffsetDateTime;
import java.util.UUID;

public record UserDTO (
    UUID id,
    String username,
    String email,
    String password,
    OffsetDateTime createdAt,
    OffsetDateTime updatedAt

){}