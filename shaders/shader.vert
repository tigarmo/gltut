#version 330 core

layout(location = 0) in vec3 vertex_pos;

uniform float angle;

out vec2 pos;

mat4 rotationMatrix(vec3 axis, float angle)
{
    axis = normalize(axis);
    float s = sin(angle);
    float c = cos(angle);
    float oc = 1.0 - c;

    return mat4(oc * axis.x * axis.x + c,           oc * axis.x * axis.y - axis.z * s,  oc * axis.z * axis.x + axis.y * s,  0.0,
                oc * axis.x * axis.y + axis.z * s,  oc * axis.y * axis.y + c,           oc * axis.y * axis.z - axis.x * s,  0.0,
                oc * axis.z * axis.x - axis.y * s,  oc * axis.y * axis.z + axis.x * s,  oc * axis.z * axis.z + c,           0.0,
                0.0,                                0.0,                                0.0,                                1.0);
}

void main(){
    vec3 axis = vec3(0.0, 0.0, 1.0);
    vec4 transformed_vertex = rotationMatrix(axis, radians(angle)) * vec4(vertex_pos * 0.5, 1.0);
    pos = transformed_vertex.xy;
    gl_Position = transformed_vertex;
}