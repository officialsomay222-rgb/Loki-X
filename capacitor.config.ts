import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.react.example',
  appName: 'react-example',
  webDir: 'dist',
  server: {
    url: 'https://loki-x.netlify.app',
    cleartext: true
  }
};

export default config;
