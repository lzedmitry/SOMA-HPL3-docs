---
title: HPSL Shading Language
description: // Example code
category: generated
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Shaders/HPSL_Shading_Language"
sourceRevision: 6831
sourceUpdated: "2024-09-12T22:17:54Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - generated
sidebar:
  hidden: true
---
<h2 class="wp-block-heading">Introduction</h2>

<p>HPL3 is our first engine to support both PC and consoles. To make it easy to support multiple platforms and multiple shading languages we have decided to use our own shading language called HPSL. Shader code written in HPSL goes through a shader parser to translate it to the language used by the hardware.</p>

<p>The shader written in HPSL is loaded into the engine at runtime, the code is then run through a preprocess parser that strips away any code that is not needed by the effect or material. After that the stripped code is translated to the language used by the hardware (GLSL #330 on PC and PSSL on the PS4) and then compiled.</p>

<p>HPSL uses the same syntax as the scripting or engine code. HPSL is based on GLSL #330 but some of the declarations are closer to HLSL.</p>

```
// Example code

@ifdef UseTexture

uniform cTexture2D aColorMap : 0;

@endif

void main(in cVector4f px_vPosition,

                in cVector4f px_vColor,

                in cVector4f px_vTexCoord0,

                out cVector4f out_vColor : 0)

{

          cVector4f vColor = px_vColor;

@ifdef UseTexture

                    vColor *= sample(aColorMap, px_vTexCoord0.xy);

          @endif

          out_vColor = vColor;

}

//Preproccess step

void main(in cVector4f px_vPosition,

                in cVector4f px_vColor,

                in cVector4f px_vTexCoord0,

                out cVector4f out_vColor : 0)

{

          cVector4f vColor = px_vColor;

          out_vColor = vColor;

}

// Translation step

#version 330

#extension GL_ARB_explicit_attrib_location : enable

in vec4 px_vColor;

in vec4 px_vTexCoord0;

layout(location = 0) out vec4 out_vColor;

void main()

{

          vec4 px_vPosition = gl_FragCoord;

          bool px_bFrontFacing = gl_FrontFacing;

          int px_lPrimitiveID = gl_PrimitiveID;

          vec4 vColor = px_vColor;

          out_vColor = vColor;

}
```

<h2 class="wp-block-heading">Preprocessing</h2>

<p>All the shader code used in SOMA is handwritten. In order to keep all the relevant code at the same place and to be able to quickly optimize shaders HPL3 uses a preprocessing step. This has been used for our previous games as well. A preprocessor goes thorugh the code and removes large chunks that are not needed or used by the effect or material. The lighting shader used in SOMA contains code used by all the different light types. Changing a preprocess variable can change a light from a point light to a spotlight or can be used to enable shadow mapping. The preprocessor strips blocks of code that are not used, this increases performance since code that has no visual effects is removed completely. Another feature of the preprocess parser is the ability to change the value of a constant variable, this can be used to change the quality of an effect.</p>

```
// SSAO code

for(float d = 0.0; d < $kNumSamples; d+=4.0)
{
          // perform SSAO…
}
```

<p>The preprocessor makes it easy to do complex materials with multiple textures and shading properties while only performing the heavy computations for the materials that need it.</p>

<h2 class="wp-block-heading">Translation</h2>

<p>After the preprocess strips the code it is ready to get translated. In the first step all the variable types and special functions are converted to the new language. Then the main entry function is created and all the input and output is bound to the correct semantics. In the last step the translated code is scanned for texture and buffers that get bound to the correct slot. </p>

<h2 class="wp-block-heading">Compilation</h2>

<p>The translated code is then compiled. If a compilation error occurred the translated code is printed to the log file along with the error message and corresponding row for easy debugging.</p>

<h2 class="wp-block-heading">Summary</h2>

<p>In order to deliver the same visual experience to all platforms and to make development faster we decided on using our own shading language. The code is translated to the language used by the hardware and compiled at runtime. Supporting other shading languages in the future will be very easy since we only need to add another converter. </p>

<p>HPSL translates to GLSL #330 which requires OpenGL 3.3 (DirectX 10 feature set). This means that SOMA will require a DirectX 10 or newer graphic card.</p>

<p>Modders will still be able to write shader code directly in GLSL if they chose to.</p>

<h2 class="wp-block-heading">HPSL Reference</h2>

<h3 class="wp-block-heading">Syntax</h3>

<p>HPSL uses the same syntax used by the scripting language.</p>

<table class=""><tr><td><strong>Variable Type</strong></td><td><strong>Description</strong></td></tr><tr><td>int</td><td>32 bit signed integer</td></tr><tr><td>uint</td><td>32 bit unsigned integer</td></tr><tr><td>bool</td><td>Stores true or false</td></tr><tr><td>float</td><td>32 bit float</td></tr><tr><td>double</td><td>64 bit float</td></tr><tr><td>cVectorXf</td><td>Vector of floats</td></tr><tr><td>cVectorXl</td><td>Vector of signed integers</td></tr><tr><td>cVectorXu</td><td>Vector of unsigned intergers</td></tr><tr><td>cMatrixXf</td><td>Square float matrix</td></tr><tr><td>cMatrixXxXf</td><td>Non-square matrix (Ex cMatrix2x4f)</td></tr><tr><td>cBuffer</td><td>Container of multiple variables that get set by the CPU</td></tr></table>

<table class=""><tr><td><strong>Texture Type</strong></td><td><strong>Description</strong></td></tr><tr><td>cTexture1D</td><td>Single dimension texture</td></tr><tr><td>cTexture2D</td><td>Standard 2D texture</td></tr><tr><td>cTexture3D</td><td>Volume texture</td></tr><tr><td>cTextureCube</td><td>Cubemap texture</td></tr><tr><td>cTextureBuffer</td><td>A large single dimension texture used to store variables</td></tr><tr><td>cTexture2DMS</td><td>A 2D render target with MSAA support</td></tr><tr><td>cTextureXCmp</td><td>A shadow map texture used for comparison operations</td></tr><tr><td>cTextureXArray</td><td>Array of cTextureX textures</td></tr></table>

<p>A texture contains both the image and information about what happens when it is sampled. If you are used to OpenGL/GLSL then this is nothing new. DirectX uses a different system for storing this information. It uses a texture for storing the data and a separate sampler_state that controls filtering and clamping. Using the combined format makes it easy to convert to either GLSL or HLSL.</p>

<p>Textures need to be bound to a slot at compilation time. Binding is done by using the “:” semantic after the texture name.</p>

```
//bind diffuse map to slot 0
uniform cTexture2D aDiffuseMap : 0;</code>
```

<table class=""><tr><td><strong>Variable Type Modifier</strong></td><td><strong>Description</strong></td></tr><tr><td>uniform</td><td>A variable or texture that is set by the CPU</td></tr><tr><td>in</td><td>Read only input to a function</td></tr><tr><td>out</td><td>Output of a function</td></tr><tr><td>inout</td><td>Read and write input and output to a function</td></tr><tr><td>const</td><td>A constant value that must be initialized in the declaration and can’t be changed</td></tr></table>

<h3 class="wp-block-heading">Entry Point and Semantics</h3>

<p>The entry point of a shader program is the “void main” function. Input and output of the shader is defined as arguments to this function. The input to the vertex shader comes from the mesh that is rendered. This might be information like the position, color and uv mapping of a vertex. What the vertex shader outputs is user defined, it can be any kind of information that the pixel shader needs. The output of the vertex shader is what gets sent to the pixel shader as input. The variables are interpolated between the vertices of the triangle. The input of the pixel shader and the output of the vertex shader must be the same or else the shaders won’t work together. Finally the output of the pixel shader is what is shown on the screen. The pixel shader can output to a of maximum 4 different render targets at the same time.</p>

<p>Some of the input and output are System defined semantics. System Semantics are set or used by the hardware. </p>

<table class=""><tr><td><strong>System Semantic</strong></td><td><strong>Description</strong></td><td><strong>Type</strong></td><td><strong>Shader Type</strong></td></tr><tr><td>px_vPosition</td><td>Vertex position output. Pixel shader input as screen position. This is required by all shaders</td><td>cVector4f</td><td>Vertex (out), Pixel (in)</td></tr><tr><td>: X</td><td>Output color slot, where X must be in the range 0-3</td><td>cVector4</td><td>Pixel (out)</td></tr><tr><td>vtx_lVertexID</td><td>Index of the current vertex</td><td>int</td><td>Vertex (in)</td></tr><tr><td>vtx_lInstanceID</td><td>Index of the current instance</td><td>int</td><td>Vertex (in)</td></tr><tr><td>px_lPrimitiveID</td><td>Index of the triangle this pixel belongs to</td><td>int</td><td>Pixel (in)</td></tr><tr><td>px_bFrontFacing</td><td>Indicates if the pixel belongs to   the front or back of the primitive</td><td>bool</td><td>Pixel (in)</td></tr></table>

<p>Input to the vertex shader is user defined. HPL3 has a few user defined semantics that work with our mesh format.</p>

<table class=""><tr><td><strong>Mesh Semantic</strong></td><td><strong>Description</strong></td><td><strong>Type</strong></td></tr><tr><td>vtx_vPosition</td><td>Position of the vertex</td><td>cVector4f</td></tr><tr><td>vtx_vTexCoord0</td><td>Primary UV coord</td><td>cVector4f</td></tr><tr><td>vtx_vTexCoord1</td><td>Secondary UV coord</td><td>cVector4f</td></tr><tr><td>vtx_vNormal</td><td>World space normal</td><td>cVector3f</td></tr><tr><td>vtx_vTangent</td><td>World space tangent, w contains binormal direction</td><td>cVector4f</td></tr><tr><td>vtx_vColor</td><td>Color</td><td>cVector4f</td></tr><tr><td>vtx_vBoneIndices</td><td>Index of the bones used to modify this vertex</td><td>cVector4l</td></tr><tr><td>vtx_vBoneWeight</td><td>Weight to multiply the bones with</td><td>cVector4f</td></tr></table>

<p>It is possible to add more user defined semantics if needed:</p>

```
//vertex shader

uniform cMatrixf a_mtxModelViewProjection;

void main(in cVector4f vtx_vPosition,

               in cVector4f vtx_vColor,

               in cVector4f vtx_vTexCoord0,

               out cVector4f px_vColor,

               out cVector4f px_vTexCoord0,

              out cVector4f px_vPosition)

{                          

          px_vPosition = mul(a_mtxModelViewProjection, vtx_vPosition);

          px_vColor = vtx_vColor;

                             px_vTexCoord0 = vtx_vTexCoord0;

}

//pixel shader

uniform cTexture2D aColorMap : 0;

void main(in cVector4f px_vPosition,

               in cVector4f px_vColor,

               in cVector4f px_vTexCoord0,

               out cVector4f out_vColor : 0)

{

         out_vColor = px_vColor * sample(aColorMap, px_vTexCoord0.xy);

}</code>
```

<h3 class="wp-block-heading">Functions</h3>

<p>HPSL is based on OpenGL 3.3 and GLSL version 330 and supports almost all of the [GLSL arithmetic functions](http://www.shaderific.com/glsl-functions/)</p>

<p>There are some functions that are different from GLSL. This is to make it easier to support HLSL and PSSL.</p>

<table class=""><tr><td><strong>Arithmetic Function</strong></td><td><strong>Description</strong></td></tr><tr><td>mul(x, y)</td><td>Multiplies two matrices together (multiplying by using * not supported for matrices)</td></tr><tr><td>lerp(x, y, t)</td><td>Interpolates between two values</td></tr></table>

<p>Texture sampling use functions specific to the HPSL language.</p>

<table class=""><tr><td><strong>Texture Function</strong></td><td><strong>Description</strong></td></tr><tr><td>sample(texture, uv)sample(texture, uv, offset)</td><td>Samples a texture at the specified uv coordinate. Can be used with an integet offset</td></tr><tr><td>sampleGather(texture, uv)sampleGather(texture, uv, offset)</td><td>Samples a texture but returns only the red component of each texel corner</td></tr><tr><td>sampleGrad(texture, uv, dx, dy)sampleGrad(texture, uv, dx, dy, offset)</td><td>Performs texture lookup with explicit gradients</td></tr><tr><td>sampleLod(texture, uv, lod)sampleLod(texture, uv, lod, offset)</td><td>Samples the texture at a specific mipmap level</td></tr><tr><td>sampleCmp(texture, uv, comp_value)sampleCmp(texture, uv, comp_value, offset)</td><td>Performs texture lookup and compares it with the comparison value and returns result</td></tr><tr><td>load(texture, position)</td><td>Gets the value of a texel at the integer position</td></tr><tr><td>getTextureSize(texture, lod)</td><td>Returns the width and height of the texture lod</td></tr><tr><td>getTextureLod(texture, uv)</td><td>Gets the lod that would get sampled if that uv coord is used</td></tr><tr><td>getTextureLevelCount</td><td>Gets the number of MipMap levels</td></tr></table>

<p>It is also possible to use language specific code directly. Some languages and graphic cards might have functions that are more optimized for those systems and then it might be a good idea to write code specific for that language.</p>

```
@ifdef Lang_GLSL
                  vec4 vModifier = vec4(lessThan(vValue, vLimit));
@else
                  cVector4f vModifier = step(vValue, vLimit);
@endif
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/Shaders/HPSL Shading Language](https://wiki.frictionalgames.com/page/HPL3/Shaders/HPSL_Shading_Language)
- Revision: `6831`
- Source update: `2024-09-12T22:17:54Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
