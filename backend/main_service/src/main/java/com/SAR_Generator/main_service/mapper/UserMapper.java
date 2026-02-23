package com.SAR_Generator.main_service.mapper;


import com.SAR_Generator.main_service.dto.UserDTO;
import com.SAR_Generator.main_service.models.User;

public class UserMapper {

    // Prevent instantiation
    private UserMapper() {}

    /* =========================
       Entity → DTO
    ========================== */
    public static UserDTO toDTO(User user) {

        if (user == null) {
            return null;
        }

        return UserDTO.builder()
                .id(user.getId())
                .username(user.getUsername())
                .email(user.getEmail())
                .createdAt(user.getCreatedAt())
                .updatedAt(user.getUpdatedAt())
                .build();
    }


    /* =========================
       DTO → Entity
    ========================== */
    public static User toEntity(UserDTO dto) {

        if (dto == null) {
            return null;
        }

        User user = new User();

        user.setId(dto.id());
        user.setUsername(dto.username());
        user.setEmail(dto.email());

        // Map password from DTO into entity so service can encode it
        user.setPasswordHash(dto.password());
        // Do NOT set timestamps (DB managed)

        return user;
    }
}