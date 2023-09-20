import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [react()],
  server: {
    host: mode === "production" ? "0.0.0.0" : "0.0.0.0",
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  build: {
    manifest: true,
    rollupOptions: {
      input: {
        main: resolve("./src/main.tsx"),
      },
    },
  },
}));
