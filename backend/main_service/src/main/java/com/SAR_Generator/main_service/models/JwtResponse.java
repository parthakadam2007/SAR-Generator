package com.SAR_Generator.main_service.models;


import java.util.UUID;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
public class JwtResponse {
    private String jwtToken;
    private String username;
    private UUID userId;
}
