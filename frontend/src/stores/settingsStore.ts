import { create } from 'zustand'
import { createJSONStorage, persist } from 'zustand/middleware'

type SettingsState = {
  age: number
  interests: string
  setAge: (age: number) => void
  setInterests: (interests: string) => void
  reset: () => void
}

export const useSettingsStore = create<SettingsState>()(
  persist(
    (set) => ({
      age: 0,
      interests: '',
      setAge: (age) => set({ age }),
      setInterests: (interests) => set({ interests }),
      reset: () => set({ age: 0, interests: '' }),
    }),
    {
      name: 'settings',
      version: 2,
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({ age: state.age, interests: state.interests }),
      migrate: (persistedState, version) => {
        if (version < 2) {
          const legacy = persistedState as { name?: string; interests?: string }
          const migrated = {
            age: 0,
            interests: legacy?.interests ?? '',
          }
          return migrated as unknown as SettingsState
        }
        return persistedState as unknown as SettingsState
      },
    }
  )
)


