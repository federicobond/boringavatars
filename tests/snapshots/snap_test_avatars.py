# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AvatarTests::test_avatar_bauhaus 1'] = '''<svg
  viewBox="0 0 80 80"
  fill="none"
  role="img"
  xmlns="http://www.w3.org/2000/svg"
  width="40"
  height="40"
>
  
  <mask id=":qQQ0lo:" maskUnits="userSpaceOnUse" x="0" y="0" width="80" height="80">
    <rect width="80" height="80" rx="160" fill="#FFFFFF" />
  </mask>
  <g mask="url(#:qQQ0lo:)">
    <rect width="80" height="80" fill="#405059" />
    <rect
      x="10.0"
      y="30.0"
      width="80"
      height="10.0"
      fill="#FFAD08"
      transform="translate(-12.0 6.0) rotate(8 40.0 40.0)"
    />
    <circle
      cx="40.0"
      cy="40.0"
      fill="#EDD75A"
      r="16.0"
      transform="translate(15.0 4.0)"
    />
    <line
      x1="0"
      y1="40.0"
      x2="80"
      y2="40.0"
      stroke-width="2"
      stroke="#73B06F"
      transform="translate(8.0 8.0) rotate(16 40.0 40.0)"
    />
  </g>
</svg>'''

snapshots['AvatarTests::test_avatar_beam 1'] = '''<svg
  viewBox="0 0 36 36"
  fill="none"
  role="img"
  xmlns="http://www.w3.org/2000/svg"
  width="40"
  height="40"
>
  
  <mask id=":qQQ0lo:" maskUnits="userSpaceOnUse" x="0" y="0" width="36" height="36">
    <rect width="36" height="36" rx="72" fill="#FFFFFF" />
  </mask>
  <g mask="url(#:qQQ0lo:)">
    <rect width="36" height="36" fill="#73B06F" />
    <rect
      x="0"
      y="0"
      width="36"
      height="36"
      transform="translate(0.0 0.0) rotate(184 18.0 18.0) scale(1.1)"
      fill="#405059"
      rx="36"
    />
    <g transform="translate(0 -1) rotate(4 18.0 18.0)">
      
        <path
          d="M15 20c2 1 4 1 6 0"
          stroke="#FFFFFF"
          fill="none"
          stroke-linecap="round"
        />
      
      <rect
        x="10"
        y="14"
        width="1.5"
        height="2"
        rx="1"
        stroke="none"
        fill="#FFFFFF"
      />
      <rect
        x="24"
        y="14"
        width="1.5"
        height="2"
        rx="1"
        stroke="none"
        fill="#FFFFFF"
      />
    </g>
  </g>
</svg>'''

snapshots['AvatarTests::test_avatar_marble 1'] = '''<svg
   viewBox="0 0 80 80"
   fill="none"
   role="img"
   xmlns="http://www.w3.org/2000/svg"
   width="40"
   height="40"
>
   
   <mask id=":qQQ0lo:" maskUnits="userSpaceOnUse" x="0" y="0" width="80" height="80">
     <rect width="80" height="80" rx="160" fill="#FFFFFF" />
   </mask>
   <g mask="url(#:qQQ0lo:)">
     <rect width="80" height="80" fill="#405059" />
     <path
       filter="url(#prefix__filter0_f)"
       d="M32.414 59.35L50.376 70.5H72.5v-71H33.728L26.5 13.381l19.057 27.08L32.414 59.35z"
       fill="#FFAD08"
       transform="translate(-0.0 -0.0) rotate(-8 40.0 40.0) scale(1.2)"
     />
     <path
       filter="url(#prefix__filter0_f)"
       style="mix-blend-mode: overlay;"
       d="M22.216 24L0 46.75l14.108 38.129L78 86l-3.081-59.276-22.378 4.005 12.972 20.186-23.35 27.395L22.215 24z"
       fill="#EDD75A"
       transform="translate(0.0 -0.0) rotate(192 40.0 40.0) scale(1.2)"
     />
   </g>
   <defs>
     <filter
       id="prefix__filter0_f"
       filterUnits="userSpaceOnUse"
       colorInterpolationFilters="sRGB"
     >
       <feFlood flood-opacity="0" result="BackgroundImageFix" />
       <feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape" />
       <feGaussianBlur stdDeviation="7" result="effect1_foregroundBlur" />
     </filter>
   </defs>
 </svg>'''

snapshots['AvatarTests::test_avatar_pixel 1'] = '''<svg
  viewBox="0 0 80 80"
  fill="none"
  role="img"
  xmlns="http://www.w3.org/2000/svg"
  width="40"
  height="40"
>
  
  <mask
    id=":qQQ0lo:"
    mask-type="alpha"
    maskUnits="userSpaceOnUse"
    x="0"
    y="0"
    width="80"
    height="80"
  >
    <rect width="80" height="80" rx="160" fill="#FFFFFF" />
  </mask>
  <g mask="url(#:qQQ0lo:)">
    <rect width="10" height="10" fill="#FFAD08" />
    <rect x="20" width="10" height="10" fill="#FFAD08" />
    <rect x="40" width="10" height="10" fill="#EDD75A" />
    <rect x="60" width="10" height="10" fill="#FFAD08" />
    <rect x="10" width="10" height="10" fill="#405059" />
    <rect x="30" width="10" height="10" fill="#405059" />
    <rect x="50" width="10" height="10" fill="#EDD75A" />
    <rect x="70" width="10" height="10" fill="#FFAD08" />
    <rect y="10" width="10" height="10" fill="#405059" />
    <rect y="20" width="10" height="10" fill="#405059" />
    <rect y="30" width="10" height="10" fill="#73B06F" />
    <rect y="40" width="10" height="10" fill="#405059" />
    <rect y="50" width="10" height="10" fill="#405059" />
    <rect y="60" width="10" height="10" fill="#0C8F8F" />
    <rect y="70" width="10" height="10" fill="#405059" />
    <rect x="20" y="10" width="10" height="10" fill="#0C8F8F" />
    <rect x="20" y="20" width="10" height="10" fill="#73B06F" />
    <rect x="20" y="30" width="10" height="10" fill="#405059" />
    <rect x="20" y="40" width="10" height="10" fill="#405059" />
    <rect x="20" y="50" width="10" height="10" fill="#405059" />
    <rect x="20" y="60" width="10" height="10" fill="#EDD75A" />
    <rect x="20" y="70" width="10" height="10" fill="#0C8F8F" />
    <rect x="40" y="10" width="10" height="10" fill="#FFAD08" />
    <rect x="40" y="20" width="10" height="10" fill="#EDD75A" />
    <rect x="40" y="30" width="10" height="10" fill="#405059" />
    <rect x="40" y="40" width="10" height="10" fill="#405059" />
    <rect x="40" y="50" width="10" height="10" fill="#73B06F" />
    <rect x="40" y="60" width="10" height="10" fill="#0C8F8F" />
    <rect x="40" y="70" width="10" height="10" fill="#73B06F" />
    <rect x="60" y="10" width="10" height="10" fill="#405059" />
    <rect x="60" y="20" width="10" height="10" fill="#405059" />
    <rect x="60" y="30" width="10" height="10" fill="#405059" />
    <rect x="60" y="40" width="10" height="10" fill="#73B06F" />
    <rect x="60" y="50" width="10" height="10" fill="#73B06F" />
    <rect x="60" y="60" width="10" height="10" fill="#405059" />
    <rect x="60" y="70" width="10" height="10" fill="#405059" />
    <rect x="10" y="10" width="10" height="10" fill="#FFAD08" />
    <rect x="10" y="20" width="10" height="10" fill="#0C8F8F" />
    <rect x="10" y="30" width="10" height="10" fill="#405059" />
    <rect x="10" y="40" width="10" height="10" fill="#405059" />
    <rect x="10" y="50" width="10" height="10" fill="#0C8F8F" />
    <rect x="10" y="60" width="10" height="10" fill="#73B06F" />
    <rect x="10" y="70" width="10" height="10" fill="#0C8F8F" />
    <rect x="30" y="10" width="10" height="10" fill="#FFAD08" />
    <rect x="30" y="20" width="10" height="10" fill="#405059" />
    <rect x="30" y="30" width="10" height="10" fill="#FFAD08" />
    <rect x="30" y="40" width="10" height="10" fill="#EDD75A" />
    <rect x="30" y="50" width="10" height="10" fill="#FFAD08" />
    <rect x="30" y="60" width="10" height="10" fill="#73B06F" />
    <rect x="30" y="70" width="10" height="10" fill="#405059" />
    <rect x="50" y="10" width="10" height="10" fill="#405059" />
    <rect x="50" y="20" width="10" height="10" fill="#405059" />
    <rect x="50" y="30" width="10" height="10" fill="#EDD75A" />
    <rect x="50" y="40" width="10" height="10" fill="#73B06F" />
    <rect x="50" y="50" width="10" height="10" fill="#405059" />
    <rect x="50" y="60" width="10" height="10" fill="#0C8F8F" />
    <rect x="50" y="70" width="10" height="10" fill="#0C8F8F" />
    <rect x="70" y="10" width="10" height="10" fill="#73B06F" />
    <rect x="70" y="20" width="10" height="10" fill="#EDD75A" />
    <rect x="70" y="30" width="10" height="10" fill="#405059" />
    <rect x="70" y="40" width="10" height="10" fill="#0C8F8F" />
    <rect x="70" y="50" width="10" height="10" fill="#FFAD08" />
    <rect x="70" y="60" width="10" height="10" fill="#73B06F" />
    <rect x="70" y="70" width="10" height="10" fill="#EDD75A" />
  </g>
</svg>'''

snapshots['AvatarTests::test_avatar_ring 1'] = '''<svg
  viewBox="0 0 90 90"
  fill="none"
  role="img"
  xmlns="http://www.w3.org/2000/svg"
  width="40"
  height="40"
>
  
  <mask id=":qQQ0lo:" maskUnits="userSpaceOnUse" x="0" y="0" width="90" height="90">
    <rect width="90" height="90" rx="180" fill="#FFFFFF" />
  </mask>
  <g mask="url(#:qQQ0lo:)">
    <path d="M0 0h90v45H0z" fill="#405059" />
    <path d="M0 45h90v45H0z" fill="#FFAD08" />
    <path d="M83 45a38 38 0 00-76 0h76z" fill="#FFAD08" />
    <path d="M83 45a38 38 0 01-76 0h76z" fill="#EDD75A" />
    <path d="M77 45a32 32 0 10-64 0h64z" fill="#EDD75A" />
    <path d="M77 45a32 32 0 11-64 0h64z" fill="#73B06F" />
    <path d="M71 45a26 26 0 00-52 0h52z" fill="#73B06F" />
    <path d="M71 45a26 26 0 01-52 0h52z" fill="#405059" />
    <circle cx="45" cy="45" r="23" fill="#0C8F8F" />
  </g>
</svg>'''

snapshots['AvatarTests::test_avatar_sunset 1'] = '''<svg
  viewBox="0 0 80 80"
  fill="none"
  role="img"
  xmlns="http://www.w3.org/2000/svg"
  width="40"
  height="40"
>
  
  <mask id=":qQQ0lo:" maskUnits="userSpaceOnUse" x="0" y="0" width="80" height="80">
    <rect width="80" height="80" rx="160" fill="#FFFFFF" />
  </mask>
  <g mask="url(#:qQQ0lo:)">
    <path fill="url(#gradient_paint0_linear_8843d7f92416211de9ebb963ff4ce28125932878)" d="M0 0h80v40H0z" />
    <path fill="url(#gradient_paint1_linear_8843d7f92416211de9ebb963ff4ce28125932878)" d="M0 40h80v40H0z" />
  </g>
  <defs>
    <linearGradient
      id="gradient_paint0_linear_8843d7f92416211de9ebb963ff4ce28125932878"
      x1="40.0"
      y1="0"
      x2="40.0"
      y2="40.0"
      gradientUnits="userSpaceOnUse"
    >
      <stop stop-color="#405059" />
      <stop offset="1" stop-color="#FFAD08" />
    </linearGradient>
    <linearGradient
      id="gradient_paint1_linear_8843d7f92416211de9ebb963ff4ce28125932878"
      x1="40.0"
      y1="40.0"
      x2="40.0"
      y2="80"
      gradientUnits="userSpaceOnUse"
    >
      <stop stop-color="#EDD75A" />
      <stop offset="1" stop-color="#73B06F" />
    </linearGradient>
  </defs>
</svg>'''
